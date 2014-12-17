from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
url(r'^add/(?P<x>\d+)/(?P<y>\d+)$', views.add, name="add"),
url(r'^about/$', views.hi, name="about"),
url(r'^contact/$', views.contact, name="contact"),
url(r'^polls/$', views.polls, name="polls"),

)
