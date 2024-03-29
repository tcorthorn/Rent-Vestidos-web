
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )


ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Rentaweb',
        'USER': 'postgres',
        'PASSWORD': '123321',
        'HOST': '127.0.0.1',
        'DATABASE_PORT':'5432',
    }
}

# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)