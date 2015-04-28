from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from exported_data.api import ExportedRevisionResource
from exported_data.views import get_lastest_data, get_lastest_checksum

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'compotista.views.home', name='home'),
    # url(r'^compotista/', include('compotista.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^latest/$', get_lastest_data),
    url(r'^latest/(?P<kind>\w+)/$', get_lastest_data),
    url(r'^latest/checksum/$', get_lastest_checksum),
    url(r'^latest/(?P<kind>\w+)/checksum/$', get_lastest_checksum),
    url(r'^api/', include(ExportedRevisionResource().urls)),
)
