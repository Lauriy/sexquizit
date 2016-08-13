from wantwillwont.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'www',
        'USER': 'www',
        'PASSWORD': 'www',
        'HOST': 'localhost',
        'PORT': '',
    }
}

EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'