from django.conf.urls import patterns, include, url
from views import home

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^export/', include('export_data.urls')),
    url(r'^api/', include('api.urls'))
)
