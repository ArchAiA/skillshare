"""
Django settings for mvp_landing project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

#! So we import the new email_info.py file that we created and set each email constant equal to the imported constant -- added in Lecture 32
#! If we wanted to import everything in email_info.py we could do this instead: [from .email_info import *]
from .email_info import EMAIL_USE_TLS, EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT

EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = EMAIL_PORT
#! So we import the new email_info.py file that we created and set each email constant equal to the imported constant -- added in Lecture 32


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) #! This takes the directory of the current file (settings.py) and goes up one level and assigns to BASE_DIR
#! /home/david/projects/skillshare/src


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h!zmj2algf9q_*h408^7-d+)#x$dx99esw)175af&!@37xcg8n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',   #! The south app was used in Lecture 31
    'signups', #! After adding the new class as a model (in models.py) you must indicate where the APP/model/class is
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mvp_landing.urls'

WSGI_APPLICATION = 'mvp_landing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


#! TEMPLATE LOCATION must be added to indicate where templates are stored
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static", "templates"), #! This will join the path of the folder that is one up from the base folder with "static", and "templates"
    #! equivalent to: /home/david/projects/skillshare/static/templates
 
)

if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only")
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
    STATICFILES_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR), "static", "static"),
    )
