"""
Django settings for itsmbc project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# AWS S3 Configuration


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-d6@q2d6ra5&0dw#6i$d6=c7yyg%$t^pd*ayin7xnf*xf35mqs7"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'storages',
    "rest_framework",
    "content",
    "content_season",
    "networks",
    'content_source',
    'episode_content_source'
]
  
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "itsmbc.urls"
import os
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
        },
    },
]
WSGI_APPLICATION = "itsmbc.wsgi.application"
ASGI_APPLICATION = 'itsmbc.asgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mbc',
        'USER': 'mbc_owner',
        'PASSWORD': 'P8VNBbXg3yZs',
        'HOST': 'ep-falling-fog-a1rbs2d1.ap-southeast-1.aws.neon.tech',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
SWAGGER_SETTINGS = {
    'DEFAULT_AUTO_SCHEMA_CLASS': 'drf_yasg.inspectors.SwaggerAutoSchema',
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        },
    },
}
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
   
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
      
    
}
# AWS S3 Settings
# AWS_ACCESS_KEY_ID = 'AKIA5I4WJHTOILINEBNX'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'itsmbc'
# AWS_S3_REGION_NAME = 'eu-north-1'


# # S3 Storage settings
# AWS_S3_FILE_OVERWRITE = False
# AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

MEDIA_URL = '/media/'
STATIC_URL = 'staticfiles/'

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL':'CLOUDINARY_URL=cloudinary://722259667259758:0XlA4eRjqQUKPAcjR5k_MGDL-7Q@dqhjy5eft',
    'CLOUD_NAME': 'dqhjy5eft',
    'API_KEY': '722259667259758',
    'API_SECRET': '0XlA4eRjqQUKPAcjR5k_MGDL-7Q'
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# FIX: Django 4.2
STORAGES = {
    # Media Files
    "default": {
        "BACKEND":'cloudinary_storage.storage.MediaCloudinaryStorage',
    },
    # CSS and JS file management
    "staticfiles": {
        "BACKEND": 'cloudinary_storage.storage.MediaCloudinaryStorage',
    }
}


