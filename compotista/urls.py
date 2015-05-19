from django.conf.urls import patterns, include, url

from export_data.api import RepresentativeRessource
# from exported_data.views import get_lastest_data, get_lastest_checksum

from views import home

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^export/', include('export_data.urls')),
    url(r'^api/', include(RepresentativeRessource().urls)),
)
