import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRIVATE_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'ensio_private')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = open(os.path.join(PRIVATE_DIR, 'secret_key'), 'r', encoding='utf8').read()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# On local debug add DOMAIN_NAME to /etc/hosts
DOMAIN_NAME = 'leoproko.io'
DOMAIN_NAME_RU = 'leoproko.ru'
DOMAIN_NAME_COM = 'leoproko.com'

ALLOWED_HOSTS = [
    DOMAIN_NAME_RU,
    DOMAIN_NAME_COM,
    '.' + DOMAIN_NAME_RU,
    '.' + DOMAIN_NAME_COM,
    '127.0.0.1',
    '195.2.70.101',
]

ROOT_HOSTCONF = 'core.hosts'
DEFAULT_HOST = 'base'
PARENT_HOST = DOMAIN_NAME_COM
HOST_PORT = '8080'
# HOST_PORT = '80'
SESSION_COOKIE_DOMAIN = '.' + DOMAIN_NAME_COM

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'docs',
    'shop',
    'crm',
    'design',
    'factory',
    'django_filters',
    'django_hosts',
]

MIDDLEWARE = [
    'django_hosts.middleware.HostsRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

AUTH_USER_MODEL = 'factory.User'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PRIVATE_DIR, 'database/db.sqlite3'),
        'USER': 'mydatauser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Logger
# https://docs.djangoproject.com/en/3.2/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/log.log'),
            'formatter': 'formatter',
        },
    },
    'formatters': {
        'formatter': {
            'format': '{levelname} {asctime} {module}: {message}',
            'style': '{',
        }
    },
    'loggers': {
        'shop': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_URL = '/static/'
# STATIC_URL = '/root/ensio/frontend_server/static/'

MEDIA_URL = '/img/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/img')
