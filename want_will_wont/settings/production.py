from want_will_wont.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['.example.com']

TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]
