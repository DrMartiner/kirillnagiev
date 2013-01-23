# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from filebrowser.sites import site
from flatblocks.views import edit

from apps.simple_page.views import MainPage, BiographyPage, ContactPage
from apps.simple_page.views import FilmList, PoetryList, VideoList, PhotoList
from apps.simple_page.views import NewsList, NewsDetail
from apps.simple_page.views import sitemaps

admin.autodiscover()

def permission_check(request, flatblock):
    return request.user.is_superuser

urlpatterns = patterns('',
    url(r'^$', MainPage.as_view(), name='main_page'),
    url(r'^contact/$', ContactPage.as_view(), name='contact_page'),
    url(r'^biography/$', BiographyPage.as_view(), name='biography_page'),

    url(r'^film/$', FilmList.as_view(), name='film_list'),
    url(r'^news/$', NewsList.as_view(), name='news_list'),
    url(r'^news/(?P<slug>[^/]+)/$', NewsDetail.as_view(), name='news_detail'),
    url(r'^poetry/$', PoetryList.as_view(), name='poetry_list'),
    url(r'^video/$', VideoList.as_view(), name='video_list'),
    url(r'^photo/$', PhotoList.as_view(), name='photo_list'),

    url(r'^robots.txt$', direct_to_template, {'template': 'robots.html', 'mimetype': 'text/plain'}),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    url(r'^flatblocks/(?P<pk>\d+)/edit/$', login_required(edit), {'permission_check': permission_check}, name='flatblocks_edit'),
    url(r'^markitup/', include('markitup.urls')),

    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/?', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True, }),
        url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True, }),
    )