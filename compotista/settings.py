# coding: utf-8

# Django settings for compotista project.

# This file is part of compotista.
#
# compotista is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or any later version.
#
# compotista is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Affero Public
# License along with compotista.
# If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2013 Laurent Peuch <cortex@worlddomination.be>
# Copyright (C) 2015 Arnaud Fabre <af@laquadrature.net>

import json
import os
# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

DATA_DIR = os.environ.get('OPENSHIFT_DATA_DIR', None)
LOG_DIR = os.environ.get('OPENSHIFT_LOG_DIR', None)
PUBLIC_DIR = os.path.join(os.environ.get('OPENSHIFT_REPO_DIR', ''), 'wsgi/static')

config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')

if os.path.isfile(config_file):
    with open(config_file) as f:
        config = json.loads(f.read())

    def get_param(setting, config=config, default=None):
        """Get the secret variable or return explicit exception."""
        try:
            return config[setting]
        except KeyError:
            if default is not None:
                return default
            error_msg = "Set the {0} config variable".format(setting)
            raise ImproperlyConfigured(error_msg)
else:
    def get_param(setting, default=None):
        return os.environ.get(setting.upper(), default)

COMPOTISTA_SERVER = get_param('compotista_server', default='http://example.com')
TOUTATIS_SERVER = get_param('toutatis_server', default='')
REDIS_DB = get_param('redis_db', default=9)

DEBUG = get_param('debug', default=False)
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

ALLOWED_HOSTS = ['*']

MANAGERS = ADMINS

# This was probably required, but I intend to fix sqlite support if required.
# When CI will be up, we'll know. Until then, commenting
#if not get_param('database_server') in ('mysql', 'postgresql'):
#    raise ImproperlyConfigured('Compotista only support mysql or postgresql')

DATABASES = {
    'default': {
        'NAME': get_param('database_name', default='db.sqlite'),
        'USER': get_param('database_user', default=''),
        'PASSWORD': get_param('database_password', default=''),
        'HOST': get_param('database_host', default=''),
        'PORT': get_param('database_port', default=''),
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

if DATA_DIR:
    DATABASES['default']['NAME'] = os.path.join(DATA_DIR, 'db.sqlite3')

try:
    if get_param('database_server') == 'mysql':
        DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
    elif get_param('database_server') == 'postgresql':
        DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
except ImproperlyConfigured:
    pass

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = get_param('time_zone', default='Europe/Brussels')

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = get_param('language_code', default='en-us')

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

if DATA_DIR:
    MEDIA_URL = '/static/media/'
    MEDIA_ROOT = os.path.join(DATA_DIR, 'media')

if PUBLIC_DIR:
    STATIC_URL = '/static/collected/'
    STATIC_ROOT = os.path.join(PUBLIC_DIR, 'collected')

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = get_param('secret_key')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'compotista.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'compotista.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    # Django - Rest - Framework
    'rest_framework',
    'representatives',
    'export_data',
    # Import modules
    'import_parltrack_representatives',
    'compotista',
)


if DEBUG:
    INSTALLED_APPS += tuple(get_param('dev_modules'))


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s[%(module)s]: %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/compotista-debug.log',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'compotista': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        'representatives': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    },
}



REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'PAGE_SIZE': 10
}

# Django 1.7 Test runner
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

try:
    from settings_local import *
except ImportError:
    pass
