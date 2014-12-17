from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pollingsite.views.home', name='home'),
    url(r'^math/', include('polls.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
