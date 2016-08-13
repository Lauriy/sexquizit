from wantwillwont.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)

SOCIALACCOUNT_QUERY_EMAIL = False

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['email'],
        'AUTH_PARAMS': {
            'access_type': 'online',
            'approval_prompt': 'auto'
        }
    }
}
