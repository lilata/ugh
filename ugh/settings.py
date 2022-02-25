"""
Django settings for ugh project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os.path
from os import environ
import warnings
from pathlib import Path
import tomli

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRETS_FILE = os.path.join(BASE_DIR, 'secrets.toml')
SECRETS = {}
if os.path.exists(SECRETS_FILE):
    with open(SECRETS_FILE, 'rb') as f:
        SECRETS.update(tomli.load(f))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = environ.get('UGH_PROD') != '1'
if DEBUG is False:
    warnings.warn("DEBUG is False.")
# SECURITY WARNING: keep the secret key used in production secret!
if DEBUG:
    SECRET_KEY = 'django-insecure-e8!*=nkrk(2o0&obdc=b4=*9d-cip6a#rs+o)*#58vyo)@m8)%'
else:
    SECRET_KEY = SECRETS.get('secret_key')
    if not SECRET_KEY:
        raise ValueError("Invalid SECRET_KEY in production environment!")



ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
if DEBUG:
    ALLOWED_HOSTS += '*'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'ugh',
    'iloveme',
    'account',
    'rest_framework',
    'utils',
    'admin_honeypot',
]
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'ugh.middleware.AdminDirectLoginMiddleware',
]

ROOT_URLCONF = 'ugh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ugh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'default_static_root')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

FAVICON_RELATIVE_PATH = 'img/favicon.ico'

EXTERNAL_FILES_DIR = os.path.join(BASE_DIR, 'externalfiles')

CAPTCHA = 'kocaptcha'
CAPTCHA_ENTRY_LIFETIME = 300
KOCAPTCHA_HOST = 'kocaptcha.lain.day'
KOCAPTCHA_AUTHORIZATION_HEADER = SECRETS.get('kocaptcha_authorization_header')
if not KOCAPTCHA_AUTHORIZATION_HEADER:
    warnings.warn('Empty kocaptcha authorization header. Authorization is disabled.')
# only works when DEBUG is False
# ---START---
ADMIN_BASE_URL = 'element/'
ADMIN_DIRECT_LOGIN_IPS = [
    '127.0.0.1',
]
ADMIN_DIRECT_LOGIN_URL = '/admin/'
ADMIN_DIRECT_LOGIN_CREATE_USER_IF_NOT_EXIST = True
# ---END---

LOGIN_URL = '/account/login/'
