from representatives.models import Representative, Mandate
from rest_framework import viewsets, filters
from representatives.serializers import RepresentativeHyperLinkedSerializer, MandateHyperLinkedSerializer, RepresentativeDetailSerializer


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
        self.serializer_class = RepresentativeHyperLinkedSerializer
        return super(RepresentativeViewSet, self).list(request)

    def retrieve(self, request, pk=None):
        self.serializer_class = RepresentativeDetailSerializer
        return super(RepresentativeViewSet, self).retrieve(request, pk)


class MandateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows mandates to be viewed.
    """
    queryset = Mandate.objects.all()
    serializer_class = MandateHyperLinkedSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = {
        'id': ['exact'],
        'group__name': ['exact', 'icontains'],
        'group__abbreviation': ['exact'],
    }
    search_fields = ('group__name', 'group__abbreviation')
    # ordering_fields = ()
