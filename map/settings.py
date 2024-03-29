"""
Django settings for check2 project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

from django.conf import global_settings
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pvqe&sy5v%+b)4z^mw6ib)iww0#epnk4clw91_d+h)p&)x0mm0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['etrss1.herokuapp.com', 'localhost', '127.0.0.1', '*']

# Application definition

INSTALLED_APPS = [
    'mapapp.apps.MapappConfig',
    'accounts.apps.AccountsConfig',
    'archives.apps.ArchivesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'map.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'map.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default':
        {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'etrss_request_db',
        }
}

# DATABASES = {
#     'default':
#          {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME':'',
#         'USER':'postgres',
#         'PASSWORD':'',
#         'HOST':'localhost',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'accounts.UserProfile'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

gettext_noop = lambda s: s

LANGUAGES = (
    ('en', _('English')),
    ('am', gettext_noop('Amharic')),
)

EXTRA_LANG_INFO = {
    'am': {
        'bidi': False,
        'code': 'am',
        'name': 'Amharic',
        'name_local': 'አማርኛ',
    },
}

import django.conf.locale

LANG_INFO = dict(django.conf.locale.LANG_INFO, **EXTRA_LANG_INFO)
django.conf.locale.LANG_INFO = LANG_INFO

LANGUAGE_CODE = 'en-us'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# Messages
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# MEDIA UPLOADS
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# # Email config
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'tsegupower@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
