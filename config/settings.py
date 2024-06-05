"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(' ')

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Installed
    'ckeditor',
    'nested_admin',
    'adminsortable2',
    'polymorphic',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'modeltranslation',

    # Created
    'apps.about_us',
    'apps.portfolio',
    'apps.services',
    'apps.contacts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',

]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', cast=int),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = "*"

CSRF_TRUSTED_ORIGINS = ['https://tatadev.pro/', 'https://www.tatadev.pro/']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SIMPLEUI_HOME_INFO = False
SIMPLEUI_HOME_ACTION = False
SIMPLEUI_HOME_QUICK = True
SIMPLEUI_DEFAULT_THEME = 'simpleui.css'
SIMPLEUI_INDEX = '#'
SIMPLEUI_LOGO = '/static/icons/LOGO.svg'
SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menus': [
        {
            'name': 'О сайте',
            'icon': 'fa fa-database',
            'url': '/admin/about_us/siteinfo/'
        },

        {

            'name': 'Страницы',
            'icon': 'fa fa-book',
            'models': [
                # {
                #     'name': 'Preload',
                #     'icon': 'fa fa-download',
                #     'models': [
                #         {
                #             'name': 'Страница Preload',
                #             'icon': 'fa fa-download',
                #             'url': '/admin/contacts/preload/'
                #         },
                #         {
                #             'name': 'Видео',
                #             'icon': 'fa fa-video',
                #             'url': '/admin/about_us/video/'
                #         },
                #
                #     ]
                # },
                {
                    'name': 'О нас',
                    'icon': 'fa fa-info-circle',
                    'models': [
                        {
                            'name': 'Страница О нас',
                            'icon': 'fa fa-file-text',
                            'url': '/admin/about_us/aboutpage/'
                        },
                        {
                            'name': 'Блоки',
                            'icon': 'fa fa-cubes',
                            'url': '/admin/about_us/contentblock/'
                        },

                    ]
                },
                {
                    'name': 'Портфолио',
                    'icon': 'fa fa-folder',
                    'models': [
                        {
                            'name': 'Страница Портфолио',
                            'icon': 'fa fa-file-text',
                            'url': '/admin/portfolio/portfoliopage/'
                        },
                        {
                            'name': 'Направление',
                            'icon': 'fa fa-arrows',
                            'url': '/admin/portfolio/portfolioduration/'
                        },
                        {
                            'name': 'Проекты',
                            'icon': 'fa fa-industry',
                            'url': '/admin/portfolio/portfolioproject/'
                        },
                    ]
                },
                {
                    'name': 'Услуги',
                    'icon': 'fa fa-user',
                    'models': [
                        {
                            'name': 'Страница Услуг',
                            'icon': 'fa fa-file-text',
                            'url': '/admin/services/servicepage/'
                        },
                        {
                            'name': 'Услуги',
                            'icon': 'fa fa-cube',
                            'url': '/admin/services/service/'
                        },

                        {
                            'name': 'Блоки сервисов',
                            'icon': 'fa fa-cubes',
                            'url': '/admin/services/contentblock/'
                        },

                    ]
                },
                {
                    'name': 'Контакты',
                    'icon': 'fa fa-address-book',
                    'url': '/admin/contacts/contact/'
                },



            ]
        },
        {
            'name': 'Заявки',
            'icon': 'fa fa-list',
            'url': '/admin/contacts/application/'
        },

    ]
}

CKEDITOR_CONFIGS = {
    'default': {
        'entities': False,
        'entities_latin': False,
        'entities_greek': False,
        'basicEntities': False,
        'extraPlugins': '',
        'removePlugins': 'all',
        'toolbar': [],
    },
}

