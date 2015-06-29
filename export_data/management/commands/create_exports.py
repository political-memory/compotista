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

from __future__ import absolute_import

import os

from django.core.management.base import BaseCommand
from django.conf import settings

from export_data.tasks import create_exports
from export_data.models import ExportedRevision

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--clean', action='store_true', default=False)
        parser.add_argument('--celery', action='store_true', default=False)

    def handle(self, *args, **options):
        if options['clean']:
            self.clean()
            return

        if options['celery']:
            create_exports.delay()
        else:
            create_exports()

    def clean(self):
        ExportedRevision.objects.all().delete()
        folder = os.path.join(settings.PROJECT_ROOT, 'var')
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception, e:
                print e
