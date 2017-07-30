"""
Django settings for freegeek project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import random
import string

try:
    from .local_settings import SECRET_KEY, DATABASES, DEBUG
except ImportError:
    SECRET_KEY, DATABASES, DEBUG = None, None, None

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def random_str(n=50):
    chars = ''.join([string.ascii_letters, string.digits, string.punctuation]
                    ).replace('\'', '').replace('"', '').replace('\\', '')
    return ''.join([random.SystemRandom().choice(chars) for i in range(n)])


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY or os.getenv('DJANGO_SECRET_KEY')
if not SECRET_KEY:
    # need to store the new key somehwere that the other gunicorn instances can find it too!
    os.environ["DJANGO_SECRET_KEY"] = random_str()
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['totalgood.org', 'localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'freegeek',
    'diary',
    'datetimewidget',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    # 'django.contrib.auth.backends.ModelBackend',
    'diary.backends.CustomUserModelBackend',
    ]

ROOT_URLCONF = 'freegeek.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'freegeek.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


if DATABASES is None:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
        'testing_db': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'testsqldb',
            'TEST': {
                'NAME': 'auto_tests'
            }
        # Postgres connection
        # 'postgres': {
        #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #     'NAME': 'freegeek',
        #     'HOST': 'localhost',
        #     'PORT': '5432',
        #     'USER': 'freegeek',
        #     'PASSWORD': 'freegeek',
        # },
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],

}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
