# -*- coding: utf-8 -*-

import os
from django.contrib import admin
from sorl.thumbnail import get_thumbnail

from flatblocks.models import FlatBlock
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

from .models import Film, Poetry, Video, News, Photo

class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'num', 'link', 'year', 'producer', 'covert', )
    list_editable = ('num', 'link', 'year', 'producer', )

    def covert(self, obj):
        link = '/static/img/film_covert.jpg'
        if obj.image:
            if not os.path.exists(obj.image.path):
                return u'<img src="%s" />' % link
            im = get_thumbnail(obj.image, '65x45', crop='center center', quality=99)
            link = im.url
        return u'<img src="%s" />' % link
    covert.short_description = 'Обложка фильма'
    covert.allow_tags = True

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('preview', 'num', 'alt')
    list_editable = ('num', 'alt')

    def preview(self, obj):
        if os.path.exists(obj.image.path):
            im = get_thumbnail(obj.image, '65x65', crop='center center', quality=99)
            return u'<img src="%s" />' % im.url
        return ''
    preview.admin_order_field = 'image'
    preview.short_description = 'Фото'
    preview.allow_tags = True

class PoetryAdmin(admin.ModelAdmin):
    list_display = ('name', 'num', 'year', )
    list_editable = ('num', 'year', )
    search_fields = ('content', )

class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'num', 'link', )
    list_editable = ('link', 'num', )

class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'num', 'pub_date', 'link', 'slug', )
    list_editable = ('num', 'pub_date', 'link', 'slug', )
    list_filter = ('pub_date', )
    search_fields = ('content', 'name', )

    prepopulated_fields = {'slug': ('name', )}

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]

admin.site.register(News, NewsAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Poetry, PoetryAdmin)

admin.site.unregister(Site)
admin.site.unregister(Group)
admin.site.unregister(FlatBlock)