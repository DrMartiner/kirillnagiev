# -*- coding: utf-8 -*-

import sys
import os.path
from os import path

try:
    from .local_settings import *
except ImportError:
    print 'Don\'t fogot create settings_local.py'

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__)) # Глобальный путь до проекта
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps')) # Путь до приложений проекта

SITE_NAME = path.basename(path.realpath(path.curdir))
SITE_ROOT = os.path.join(path.realpath(path.pardir), SITE_NAME)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
#    ('Kuzmin Alexey', 'DrMartiner@GMail.Com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

USE_TZ = True
TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'media'))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'static'))
STATICFILES_DIRS = ()

GRAPPELLI_ADMIN_TITLE = u'Кирилл Нагиев'
ADMIN_MEDIA_PREFIX = '/static/grappelli/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = ''

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
if not DEBUG:
    TEMPLATE_LOADERS += ('django.template.loaders.eggs.Loader', )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'constance.context_processors.config',
)

ROOT_URLCONF = 'kirillnagiev.urls'

WSGI_APPLICATION = 'kirillnagiev.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.markup',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',

    'constance.backends.database',
    'constance',
    'markitup',
    'flatblocks',
    'sorl.thumbnail',

    'apps.simple_page',
)

DIRECTORY = 'filebrowser'
FILEBROWSER_DIRECTORY = 'filebrowser'

MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True})
MARKITUP_FILTER = ('django.contrib.markup.templatetags.markup.textile', {})

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_CONFIG = {
    'SITE_SHOW_POETRY': ('True', u'True - показывать; False - не показвапть'),
    'CONTACT_EMAIL': ('nagiev.k@gmail.com', u'Почта'),
    'CONTACT_AGEN_NAME': (u'Анна Кеворкова, <strong>"Актерское агенство №1"</strong>', u'Имя агента'),
    'CONTACT_PHONE': ('+7 (921) 965 78 45', u'Телефон'),
    'CONTACT_SOCIAL_FB_LINK': ('https://ru-ru.facebook.com/nagiev.k', u'Ссылка на FaceBook'),
    'CONTACT_SOCIAL_VK_LINK': ('http://vk.com/id559255', u'Ссылка на Vkontakte'),
    'CONTACT_SOCIAL_TWITTER_LINK': ('https://twitter.com/NagievKirill', u'Ссылка на Twitter'),
    'CONTACT_SOCIAL_TWITTER_WIDGET': ("""<a class="twitter-timeline" data-dnt=true href="https://twitter.com/NagievKirill" data-widget-id="285161088876675072">Твиты пользователя @NagievKirill</a><script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>""", u'Текст виджета'),
    'CONTACT_SOCIAL_INSTAGRAM_LINK': ('http://instagram.com/kirill_nagiev', u'Ссылка на Instagram'),
    'CONTACT_SOCIAL_KINOPOISK_LINK': ('http://www.kinopoisk.ru/name/1746394/', u'Ссылка на Кинопоиск'),
    'SEO_KEYWORDS': (u'Нагиев, Кирилл Нагиев, Кирилл Дмитриевич Нагиев, Дмитрий Нагиев, сын Дмитрия Нагиева, Алиса Шер,  Актер, Театр, Кино, Кинематограф, Спектакль, Антреприза, Биография, Фильмография,', u'Ключевые слова'),
    'SEO_DESCRIPTION': (u'Сайт Кирилла Нагиева сына Дмитрия Нагиева', u'Описание сайта'),
}

try:
    from .local_settings import *
except ImportError:
    pass