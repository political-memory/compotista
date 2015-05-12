from tastypie.resources import ModelResource
from .models import ExportedRevision


class ExportedRevisionResource(ModelResource):
    class Meta:
        queryset = ExportedRevision.objects.all()
        resource_name = 'exported_revision'
