from django.conf.urls import patterns, include, url

from exported_data.api import ExportedRevisionResource
from exported_data.views import get_lastest_data, get_lastest_checksum

from views import home

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^latest/$', get_lastest_data),
    url(r'^latest/(?P<kind>\w+)/$', get_lastest_data),
    url(r'^latest/checksum/$', get_lastest_checksum),
    url(r'^latest/(?P<kind>\w+)/checksum/$', get_lastest_checksum),
    url(r'^api/', include(ExportedRevisionResource().urls)),
)
