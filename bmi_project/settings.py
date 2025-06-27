# Django settings for bmi_project project.

from pathlib import Path
import os # <-- Добавьте этот импорт

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-qe_m8brdjo%409np(qlo#lajrlc#8q+s=_sjzzxvh)um(bx0we' # <-- УДАЛИТЕ ЭТУ СТРОКУ

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # <-- Оставьте False для продакшена

# Получаем SECRET_KEY из переменной окружения
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your_long_random_default_key_for_development_only')
# <-- Замените 'your_long_random_default_key_for_development_only' на длинную случайную строку
# и убедитесь, что 'DJANGO_SECRET_KEY' установлен в Railway Variables.

ALLOWED_HOSTS = ['ваше_имя_приложения.up.railway.app'] # <-- ИСПРАВЛЕНО: Укажите домен Railway
# Если вы хотите тестировать локально, можете добавить '127.0.0.1':
# ALLOWED_HOSTS = ['127.0.0.1', 'ваше_имя_приложения.up.railway.app']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bmi_calculator', # <-- ИСПРАВЛЕНО: имя вашего приложения, судя по структуре
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

ROOT_URLCONF = 'bmi_project_main.urls' # <-- ИСПРАВЛЕНО: имя вашей основной папки проекта

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'bmi_project_main.wsgi.application' # <-- ИСПРАВЛЕНО: имя вашей основной папки проекта


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
# Дополнительно для продакшена:
STATIC_ROOT = BASE_DIR / 'staticfiles' # Создает папку 'staticfiles' для сбора статики


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'