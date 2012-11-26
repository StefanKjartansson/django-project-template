INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'compressor',
    'django_extensions',
    'debug_toolbar',
    'south',
    'djcelery',
    'djangojs',
)

INSTALLED_APPS += (
    '{{ project_name }}',
)

import djcelery
djcelery.setup_loader()


BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
