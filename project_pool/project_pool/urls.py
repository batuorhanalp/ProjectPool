from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_pool.views.home', name='home'),
    url(r'^ideas/', include('pool.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
