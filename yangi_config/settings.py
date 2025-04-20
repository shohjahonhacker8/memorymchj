"""
Django settings for yangi_config project.
"""

import os
from pathlib import Path

# Loyiha ildiz papkasi
BASE_DIR = Path(__file__).resolve().parent.parent

# Xavfsizlik uchun tasodifiy kalit (mahalliy sinov uchun)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-your-secret-key-here')

# Debug rejimi mahalliy kompyuterda yoqilgan bo‘lishi kerak
DEBUG = True  # Mahalliy sinov uchun True, deploy qilganda False qilish kerak

# Ruxsat berilgan hostlar
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # Deploy qilganda Render domenini qo‘shing

# Ilovalar ro‘yxati
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'yangi_ilova',
]

# Middleware sozlamalari
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL sozlamalari
ROOT_URLCONF = 'yangi_config.urls'

# Shablon sozlamalari
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
            ],
        },
    },
]

# WSGI ilovasi
WSGI_APPLICATION = 'yangi_config.wsgi.application'

# Baza sozlamalari (mahalliy sinov uchun SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Parol validatorlari
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

# Til va vaqt mintaqasi
LANGUAGE_CODE = 'uz'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

# Statik fayllar sozlamalari
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "yangi_ilova/static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Statik fayllarni saqlash (mahalliy sinov uchun oddiy storage)
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Avtomatik maydon turi
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email sozlamalari (agar foydalanmasangiz, o‘chirib qo‘yishingiz mumkin)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'sizning.email@gmail.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'sizning.parol')