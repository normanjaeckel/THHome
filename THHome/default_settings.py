# -*- coding: utf-8 -*-

"""
Django settings.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'constance',
    'constance.backends.database',
    'THHome',
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

ROOT_URLCONF = 'THHome.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'constance.context_processors.config',
            ],
        },
    },
]

WSGI_APPLICATION = ''


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'db.sqlite3')
    }
}

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'thhome',
#        'USER': 'thhome',
#        'PASSWORD': '...',
#        'HOST': 'localhost',
#        'PORT': '5432'
#    }
# }


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'UserAttributeSimilarityValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'MinimumLengthValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'CommonPasswordValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation.'
                 'NumericPasswordValidator'),
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'de-DE'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')


# Constance - Dynamic Django settings
# http://django-constance.readthedocs.io/en/latest/

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {
    'TITLE': (
        'Titel der Seite',
        u'Titel der Seite. Wird im Browserkopf und in der Kopfzeile der Seite '
        u'verwendet.'),
    'HEADLINE': (
        'Kopfzeile',
        u'Kopfzeile auf der Startseite. HTML-Tags sind möglich.'),
    'SUB_HEADLINE': (
        'Untertitel unter der Kopfzeile',
        u'Text unter der Kopfzeile auf der Startseite. HTML-Tags sind '
        u'möglich.'),
    'HEADER_IMAGE': (
        'img/header.jpg',
        u'Pfad unterhalb des Ordners mit den statischen Dateien.'),
    'CONTACT_PHONE': (
        '0123 45 67 89 0 <br> 0987 65 43 21 0',
        u'Telefonnummer im Bereich Kontakt. HTML-Tags sind möglich.'),
    'CONTACT_MAIL': (
        'mail@example.com',
        u'E-Mail-Adresse im Bereich Kontakt. HTML-Tags sind möglich.'),
    'LEGAL_NOTICE': (
        'XY GmbH & Co. KG · Musterstraße 1 · 04333 Musterstadt',
        u'Text im Impressumsbereich. Leerzeilen erzeugen neue Absätze.'),
    'LEGAL_NOTICE_DISCLAIMER': (
        '<p>Haftung für Inhalte, Links und Hinweise zum Urheberrecht ...</p>',
        u'Text im Bereich Haftungsausschluss (Disclaimer) und '
        u'Datenschutzerklärung. HTML-Tags sind möglich.'),
    'LOCATION_IFRAME': (
        '<iframe src=""></iframe>',
        u'Iframe-Tag für eine eingebettete Karte wie von Google-Maps oder '
        u'OpenStreetMap.'),
}
