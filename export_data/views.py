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

from .models import ExportedRevision
from django.http import HttpResponse, HttpResponseNotFound

def get_lastest_data(request, kind=None):
    exported_revision = ExportedRevision.objects.filter(kind=kind)
    if not exported_revision:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return HttpResponse(exported_revision.latest('last_check_datetime').data)


def get_lastest_checksum(request, kind=None):
    exported_revision = ExportedRevision.objects.filter(kind=kind)
    if not exported_revision:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    return HttpResponse(exported_revision.latest('last_check_datetime').checksum)
