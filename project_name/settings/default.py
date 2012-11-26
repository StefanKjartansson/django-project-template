#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import absolute_import, unicode_literals

from .paths import root_path, APPNAME


ADMINS = (
    ('Stefan Kjartansson', 'esteban.supreme@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Atlantic/Reykjavik'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = root_path('media')
MEDIA_URL = '/media/'

SECRET_KEY = '{{ secret_key }}'

ROOT_URLCONF = '%s.urls' % APPNAME
WSGI_APPLICATION = '%s.wsgi.application' % APPNAME
