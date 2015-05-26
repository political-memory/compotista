from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from representatives.models import Representative, Mandate

class MandateRessource(ModelResource):
    group = fields.CharField(attribute='group__name')
    group_abbreviation = fields.CharField(attribute='group__abbreviation', null=True)
    group_kind = fields.CharField(attribute='group__kind')
    constituency = fields.CharField(attribute='constituency__name')
    
    class Meta:
        queryset = Mandate.objects.all()
        allowed_methods = ['get']
        resource_name = 'mandates'
    
class RepresentativeRessource(ModelResource):

    mandates = fields.ToManyField(
        MandateRessource,
        'mandate_set',
        full=True,
        null=True,
        use_in='detail'
    )

    cv = fields.CharField(use_in='detail', attribute='cv')
    gender = fields.CharField(attribute='gender_as_str')

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
