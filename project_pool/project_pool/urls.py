from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Auth related.
    url(r'^cikis-yap/?$', 'django.contrib.auth.views.logout', {
        'template_name': 'pool/auth/logged_out.html',
        'redirect_field_name': settings.REDIRECT_FIELD_NAME,
        'next_page': '/',
    }, name='auth_logout'),

    # Pool
    url(r'^', include('pool.urls', namespace='pool')),

    url(r'^', include('allauth.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
