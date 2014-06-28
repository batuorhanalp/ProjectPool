from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

INSTALLED_APPS += (
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

WSGI_APPLICATION = 'project_pool.wsgi.production.application'
