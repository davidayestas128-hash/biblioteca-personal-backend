"""
Configuración de Django para el proyecto config.

Generado por 'django-admin startproject' usando Django 6.1.1.

Para más información sobre este archivo, ver:
https://docs.djangoproject.com/en/6.1/topics/settings/

Para la lista completa de configuraciones y sus valores, ver:
https://docs.djangoproject.com/en/6.1/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Construye rutas dentro del proyecto de esta forma: BASE_DIR / 'subcarpeta'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

# Configuración rápida de desarrollo - no apta para producción
# Ver https://docs.djangoproject.com/en/6.1/howto/deployment/checklist/

# ADVERTENCIA DE SEGURIDAD: ¡mantén en secreto la clave usada en producción!
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-change-me-in-env')

# ADVERTENCIA DE SEGURIDAD: no actives el modo debug en producción!
DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')


# Definición de aplicaciones

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Terceros
    'rest_framework',
    'corsheaders',
    # Apps propias del proyecto
    'libros',
    'colecciones',
    'resenas',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = os.getenv(
    'CORS_ALLOWED_ORIGINS', 'http://localhost:5173'
).split(',')

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Base de datos
# https://docs.djangoproject.com/en/6.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validación de contraseñas
# https://docs.djangoproject.com/en/6.1/ref/settings/#auth-password-validators

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


# Internacionalización
# https://docs.djangoproject.com/en/6.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Archivos estáticos (CSS, JavaScript, Imágenes)
# https://docs.djangoproject.com/en/6.1/howto/static-files/

STATIC_URL = 'static/'


# Correo electrónico
# https://docs.djangoproject.com/en/6.1/topics/email/#topic-email-configuration

MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}
