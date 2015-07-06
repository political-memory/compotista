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
# License along with django-representatives.
# If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2015 Arnaud Fabre <af@laquadrature.net>

from representatives.models import Representative, Mandate, Group, Constituency
from rest_framework import viewsets, filters

from representatives.serializers import RepresentativeSerializer, RepresentativeDetailSerializer, MandateSerializer, ConstituencySerializer, GroupSerializer


class RepresentativeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows representatives to be viewed.
    """
    queryset = Representative.objects.all()
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = {
        'active': ['exact'],
        'slug': ['exact', 'icontains'],
        'id': ['exact'],
        'remote_id': ['exact'],
        'first_name': ['exact', 'icontains'],
        'last_name' : ['exact', 'icontains'],
        'full_name': ['exact', 'icontains'],
        'gender': ['exact'],
        'birth_place': ['exact'],
        'birth_date': ['exact', 'gte', 'lte'],
    }
    search_fields = ('first_name', 'last_name', 'slug')
    ordering_fields = ('id', 'birth_date', 'last_name', 'full_name')
    
    def list(self, request):
        self.serializer_class = RepresentativeSerializer
        return super(RepresentativeViewSet, self).list(request)

    def retrieve(self, request, pk=None):
        self.serializer_class = RepresentativeDetailSerializer
        return super(RepresentativeViewSet, self).retrieve(request, pk)


class MandateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows mandates to be viewed.
    """
    queryset = Mandate.objects.all()
    serializer_class = MandateSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = {
        'id': ['exact'],
        'group__name': ['exact', 'icontains'],
        'group__abbreviation': ['exact'],
    }
    search_fields = ('group__name', 'group__abbreviation')
    # ordering_fields = ()


class ConstituencyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Constituency.objects.all()
    serializer_class = ConstituencySerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
