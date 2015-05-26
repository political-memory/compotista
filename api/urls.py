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

# coding: utf-8

from django.conf.urls import patterns, url, include

from tastypie.api import Api
from api import MandateRessource, RepresentativeRessource

v1_api = Api(api_name='v1')
v1_api.register(MandateRessource())
v1_api.register(RepresentativeRessource())

urlpatterns = patterns('',
    url(r'^', include(v1_api.urls)),
)
