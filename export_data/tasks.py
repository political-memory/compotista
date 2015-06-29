# coding: utf-8

# This file is part of memopol.
#
# memopol is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or any later version.
#
# memopol is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Affero Public
# License along with django-representatives.
# If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2015 Arnaud Fabre <af@laquadrature.net>

from __future__ import absolute_import

import json
import hashlib
import os

from django.utils import timezone
from django.conf import settings

from celery import shared_task

from representatives.tasks import export_representatives
from export_data.models import ExportedRevision


@shared_task
def create_exports():
    create_export(json.dumps(
        export_representatives(), indent=4))
    create_export(json.dumps(
        export_representatives(active=True), indent=4), 'active')

def create_export(data, kind=None):
    checksum = hashlib.sha256(data).hexdigest()
    exported_revision = ExportedRevision.objects.filter(checksum=checksum)

    now = timezone.now()

    if exported_revision:
        exported_revision = exported_revision[0]
        exported_revision.last_check_datetime = now
        exported_revision.kind = kind
        exported_revision.save()
    else:
        path = os.path.join(settings.PROJECT_ROOT, 'var', str(now.date()) + checksum[:32])
        with open(path, 'w+') as f:
            f.write(data)

        ExportedRevision.objects.create(
            path=path,
            kind=kind,
            checksum=hashlib.sha256(data).hexdigest(),
            creation_datetime=now,
            last_check_datetime=now
        )
