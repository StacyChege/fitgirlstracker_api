"""
Django settings for fitgirlstracker project.
Configured for production deployment.
"""

from pathlib import Path
import os
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================================
# PRODUCTION SETTINGS
#
# These settings will be configured using environment variables.
# =========================================================================

# The SECRET_KEY is crucial for security and must be kept secret.
# In production, it will be read from an environment variable.
SECRET_KEY = os.environ.get('SECRET_KEY')
# If SECRET_KEY is not found in environment variables, fall back to a default (for local dev only).
if not SECRET_KEY:
    SECRET_KEY = 'your-local-secret-key'


DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# =========================================================================
# APPLICATION DEFINITION
# =========================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise must be listed after SecurityMiddleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fitgirlstracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fitgirlstracker.wsgi.application'


# =========================================================================
# DATABASE CONFIGURATION
#
# Connects to an external database (e.g., MySQL or PostgreSQL) in production.
# In development, it falls back to the local SQLite file.
# =========================================================================

if 'DATABASE_URL' in os.environ:
    DATABASES = {'default': dj_database_url.config(conn_max_age=600)}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# =========================================================================
# PASSWORD VALIDATION
# =========================================================================

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


# =========================================================================
# INTERNATIONALIZATION
# =========================================================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# =========================================================================
# STATIC FILES CONFIGURATION
#
# WhiteNoise handles serving static files in production.
# =========================================================================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'


# =========================================================================
# REST FRAMEWORK SETTINGS
# =========================================================================

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

# =========================================================================
# OTHER SETTINGS
# =========================================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'