from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5+f#!xn=hj^u#=cr9@pz@@5cf7bqf0ymy=8uyfpx_zvxpght3='

ADMINS = (
    ('Michael Yin', 'admin@michaelyin.info'),
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s] %(message)s",
        },
    },
    'handlers': {
        'file_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs/django.log"),
            'maxBytes': 1024*1024*5, # 5 MB,
            'backupCount': 1,
            'formatter': 'standard',
        },
    },
    'loggers': {
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['file_handler',],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {
            'handlers': ['file_handler',],
            'level': 'DEBUG',  # Or maybe INFO or DEBUG
            'propagate': False
        },
    }
}

try:
    from .local import *
except ImportError:
    pass
