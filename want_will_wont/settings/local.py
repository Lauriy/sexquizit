from want_will_wont.settings.base import *

INSTALLED_APPS += ('debug_toolbar', 'rosetta')

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

INTERNAL_IPS = (
    '127.0.0.1',
    '10.0.2.2',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
    'HIDE_DJANGO_SQL': False,
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME', 'wantwillwont_dev'),
        'USER': os.getenv('DATABASE_USER', 'wantwillwont'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'd26ec1805f28f3af6d51c6c2b72bc005'),
        'HOST': os.getenv('DATABASE_HOST', '46.101.238.121'),
        'PORT': os.getenv('DATABASE_PORT', ''),
    }
}