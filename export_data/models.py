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
# License along with compotista.
# If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2013 Laurent Peuch <cortex@worlddomination.be>
# Copyright (C) 2015 Arnaud Fabre <af@laquadrature.net>


from django.db import models

class ExportedRevision(models.Model):
    data = models.TextField()
    checksum = models.CharField(max_length=255, unique=True)
    creation_datetime = models.DateTimeField()
    last_check_datetime = models.DateTimeField()

    kind = models.CharField(max_length=128, null=True)

    class Meta:
        ordering = ['-last_check_datetime']
