
import os
import django_heroku
import boto3
from botocore.client import Config
from .data import Secret_key, Email, Email_Pass, Postgrey_Pass, AWS_ACCESS_KEY, AWS_SECRET_ACCESS, AWS_STORAGE_BUCKET

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = Secret_key

DEBUG = False

ALLOWED_HOSTS = ['locahost', 'vision--board.herokuapp.com', '13.233.250.240']
# https://vision--board.herokuapp.com/


# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    # Other Apps
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'crispy_forms',
    'storages',
    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'social_django',

    # My Apps
    'home.apps.HomeConfig',
    'users.apps.UsersConfig',
    'board.apps.BoardConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
 'django.contrib.auth.backends.ModelBackend',
 'allauth.account.auth_backends.AuthenticationBackend',
 )

ROOT_URLCONF = 'VissionBoard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

WSGI_APPLICATION = 'VissionBoard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "visionboard",
        "USER": "postgres",
        "PASSWORD": Postgrey_Pass,
        "HOST": "localhost",
        "PORT": "5432",
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

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

# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
# )
# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


AUTH_USER_MODEL = 'users.User'


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATICFILES_STORAGE = 'whitenoise.django.gzipmanifeststaticfilesstorage'
# 'whitenoise.django.gzipmanifeststaticfilesstorage'
# 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/').replace('\\', '/')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "board/static/").replace('\\', '/'),
    os.path.join(BASE_DIR, "home/static/").replace('\\', '/')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR + '/media/').replace('\\', '/')
# .replace('/', '\\')

CRISPY_TEMPLATE_PACK = 'bootstrap4'


LOGIN_REDIRECT_URL = 'home-home'
LOGIN_URL = 'users-login'
LOGOUT_URL = 'users-logout'


ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = Email
EMAIL_HOST_PASSWORD = Email_Pass


AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS
AWS_STORAGE_BUCKET_NAME = AWS_STORAGE_BUCKET
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = "ap-south-1"
# AWS_S3_HOST = "s3.ap-south-1.amazonaws.com"
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


django_heroku.settings(locals())
