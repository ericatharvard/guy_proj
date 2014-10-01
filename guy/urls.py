from django.conf.urls import patterns, url

from guy import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<guy_id>\d+)/$', views.display, name='display'),
                       url(r'^(?P<guy_id>\d+)/c/(?P<command>f|b|l|r|s)/$', views.handle_command, name='handle_command'),
                       )
