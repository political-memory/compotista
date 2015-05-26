from django.conf.urls import patterns, url, include

from tastypie.api import Api
from api import MandateRessource, RepresentativeRessource

v1_api = Api(api_name='v1')
v1_api.register(MandateRessource())
v1_api.register(RepresentativeRessource())

urlpatterns = patterns('',
    url(r'^', include(v1_api.urls)),
)
