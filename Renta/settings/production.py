
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )


ALLOWED_HOSTS = ['rentaweb.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd32k779tmo0qll',
        'USER': 'dnkkykanbxtmdh',
        'PASSWORD': '905c1a4eb9f74b05d521aee0103bc19e283980ea36340773cf426f495e402f50',
        'HOST': 'ec2-44-196-223-128.compute-1.amazonaws.com',
        'DATABASE_PORT':'5432',
    }
}

# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

