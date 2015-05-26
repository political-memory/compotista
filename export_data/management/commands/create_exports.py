# coding: utf-8

# This file is part of compotista.
#
# compotista is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or any later version.
#
# compotista is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Affero Public
# License along with Foobar.
# If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2013 Laurent Peuch <cortex@worlddomination.be>
# Copyright (C) 2015 Arnaud Fabre <af@laquadrature.net>

import json
import hashlib

from django.utils import timezone
from django.core.management.base import BaseCommand

from representatives.utils import export_all_representatives, export_active_representatives
from export_data.models import ExportedRevision

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.create_export(json.dumps(export_all_representatives(), indent=4))
        self.create_export(json.dumps(export_active_representatives(), indent=4), 'active')

    def create_export(self, data, kind=None):
        checksum = hashlib.sha256(data).hexdigest()
        exported_revision = ExportedRevision.objects.filter(checksum=checksum)

        now = timezone.now()

        if exported_revision:
            exported_revision = exported_revision[0]
            exported_revision.last_check_datetime = now
            exported_revision.kind = kind
            exported_revision.save()
        else:
            ExportedRevision.objects.create(
                data=data,
                kind=kind,
                checksum=hashlib.sha256(data).hexdigest(),
                creation_datetime=now,
                last_check_datetime=now
            )
