from pathlib import Path
import os
from google.oauth2 import service_account

BASE_DIR = Path(__file__).resolve().parent.parent

def load_env_vars(env_file_path):
    with open(env_file_path, 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

load_env_vars(os.path.join(BASE_DIR, '.env'))

DEBUG = os.environ.get('DEBUG', True) == 'True'


if DEBUG == True:
    ALLOWED_HOSTS = ['*']
    SECRET_KEY = 'django-3dl*sfe=vycqj5q@-8d5q-pzs'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    ALLOWED_HOSTS = ['blackstackhub.com']
    SECRET_KEY = os.getenv('SECRET')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'blackstackhub',
            'USER': 'blackstackhub',
            'PASSWORD': 'password123',
            'HOST': 'localhost',
        }
    }


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blackstackhub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
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

WSGI_APPLICATION = 'blackstackhub.wsgi.application'

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'blackstackhub'
GS_PROJECT_ID = 'blackstackhub'
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR, 'blackstackhub.json')
)

STATIC_URL = '/static/'
STATIC_ROOT ='static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'statics')
]

MEDIA_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
