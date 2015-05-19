from tastypie.resources import ModelResource
from tastypie.constants import ALL
from representatives.models import Representative

class RepresentativeRessource(ModelResource):
    
    class Meta:
        queryset = Representative.objects.all()
        allowed_methods = ['get']
        resource_name = 'representatives'
        filtering = {
            'slug': ALL,
            'remote_id': ALL,
            'first_name': ALL,
            'last_name': ALL,
            'full_name': ALL,
            'gender': ALL,
            'birth_place': ALL,
            'birth_date': ALL,
            'active': ALL
        }        
