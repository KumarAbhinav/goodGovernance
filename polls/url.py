from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^abhinav/$', views.abhinav, name='abhinav'),
    url(r'^\d+/$', views.index, name='abhinav')
)