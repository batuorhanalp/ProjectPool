from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Auth related.
                       (r'^accounts/', include('allauth.urls')),
    url(r'^giris-yap/?$', 'django.contrib.auth.views.login', {
        'template_name': 'pool/auth/login.html',
        'redirect_field_name': settings.REDIRECT_FIELD_NAME
    }, name='auth_login'),
    url(r'^cikis-yap/?$', 'django.contrib.auth.views.logout', {
        'template_name': 'pool/auth/logged_out.html',
        'redirect_field_name': settings.REDIRECT_FIELD_NAME,
        'next_page': '/',
    }, name='auth_logout'),

    # Pool
    url(r'^', include('pool.urls', namespace='pool')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
