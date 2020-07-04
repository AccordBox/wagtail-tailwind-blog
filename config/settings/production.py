from __future__ import absolute_import, unicode_literals

import os

from .base import *

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

try:
    from .local import *
except ImportError:
    pass
