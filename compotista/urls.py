from django.conf.urls import patterns, include, url

from export_data.api import ExportedRevisionResource
# from exported_data.views import get_lastest_data, get_lastest_checksum

from views import home

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^export/', include('export_data.urls')),
    # url(r'^latest/checksum/$', get_lastest_checksum),
    # url(r'^latest/(?P<kind>\w+)/checksum/$', get_lastest_checksum),    
    # url(r'^latest/$', get_lastest_data),
    # url(r'^latest/(?P<kind>\w+)/$', get_lastest_data),
    
    url(r'^api/', include(ExportedRevisionResource().urls)),
)
