from django.conf.urls import patterns, url

from guy import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<guy_id>[0-9]+)/$', views.display, name='display'),
                       )
