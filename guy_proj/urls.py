from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^guy/$', include('guy.urls', namespace="guy")),
                       url(r'^admin/', include(admin.site.urls)),
                       )
