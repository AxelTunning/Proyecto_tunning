from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',  # Puedes ajustar el nivel de log aquí según tu necesidad (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            'class': 'logging.FileHandler',
            'filename': 'django.log',  # El archivo donde se guardarán los registros
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}


DATABASES = {
        'default': {
            'ENGINE': 'mssql',
            'NAME': 'OPER_PRUEBAS',
            'USER': 'operaciones',
            'PASSWORD': 'operaciones',
            'HOST': '192.168.1.14',
            'PORT': '',

            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
            },
        },
    }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']


#STATIC_URL = '/static/'
#STATICFILES_DIRS = [BASE_DIR / 'static']

#STATICFILES_DIR =[BASE_DIR.child('static')]