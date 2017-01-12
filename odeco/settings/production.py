"""Production settings and globals."""

from __future__ import absolute_import

import os
from .base import *

if not DEBUG:
    ########## MANAGER CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
    ADMINS = (
        (os.environ['ADMIN_NAME'], os.environ['ADMIN_EMAIL']),
    )
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
    MANAGERS = ADMINS
    ########## END MANAGER CONFIGURATION

    ALLOWED_HOSTS = ['*']

    INSTALLED_APPS += (
        'storages',
    )

    ########## STATIC FILE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root

    # STATIC_ROOT = normpath(join(dirname(SITE_ROOT), 'static_cdn'))
    # MEDIA_ROOT = normpath(join(dirname(SITE_ROOT), 'media_cdn'))

    # STATIC_ROOT = normpath(join(SITE_ROOT, "static"))
    # MEDIA_ROOT = normpath(join(SITE_ROOT, "media"))

    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

    AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

    ########## END STATIC FILE CONFIGURATION


    ########## DATABASE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ['DB_PASSWORD'],
            'HOST': os.environ['DB_HOST'],
            'PORT': "3306",
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            }
        }
    }
    ########## END DATABASE CONFIGURATION



    ########## EMAIL CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
    EMAIL_HOST = os.environ['EMAIL_HOST']

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
    EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
    EMAIL_PORT = os.environ['EMAIL_PORT']

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
    EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
    EMAIL_USE_TLS = os.environ['EMAIL_TLS']

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
    SERVER_EMAIL = EMAIL_HOST_USER
    ########## END EMAIL CONFIGURATION


    ########## EMAIL ODECO VENTAS CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend

    # 'EMAIL_IS_LOCAL'
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
    EMAIL_HOST_ODECO = os.environ['EMAIL_HOST_ODECO_VENTAS']

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
    EMAIL_HOST_PASSWORD_ODECO = os.environ['EMAIL_HOST_PASSWORD_ODECO_VENTAS']

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
    EMAIL_HOST_USER_ODECO = os.environ['EMAIL_HOST_USER_ODECO_VENTAS']

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
    EMAIL_PORT_ODECO = os.environ['EMAIL_PORT_ODECO_VENTAS']

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
    EMAIL_USE_TLS_ODECO = os.environ['EMAIL_TLS_ODECO_VENTAS']

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
    SERVER_EMAIL_ODECO = EMAIL_HOST_USER_ODECO
    ########## END EMAIL CONFIGURATION


    # ########## CACHE CONFIGURATION
    # # See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
    # CACHES = {}
    # ########## END CACHE CONFIGURATION
