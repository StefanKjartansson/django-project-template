#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .settings import *  # noqa

INSTALLED_APPS += ('django_nose',)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['{{ project_name }}',
    '--failed',
    '--stop',
    '--with-coverage',
    '--cover-erase',
    '--cover-package={{ project_name }}',
    '--nologcapture',
    '--logging-clear-handlers',
]

BROKER_BACKEND = 'memory'
CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
