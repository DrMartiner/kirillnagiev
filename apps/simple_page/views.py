# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from flatblocks.models import FlatBlock
from .models import Film, Poetry, Video, News

class MainPage(TemplateView):
    template_name = 'simple_page/main_page.html'


class ContactPage(TemplateView):
    template_name = 'simple_page/contact.html'

class BiographyPage(TemplateView):
    template_name = 'simple_page/biography.html'

    def get_context_data(self, **kwargs):
        ctx = super(BiographyPage, self).get_context_data(**kwargs)
        ctx['flatblock'] = get_object_or_404(FlatBlock, slug='biography')
        return ctx


class FilmList(ListView):
    model = Film
    context_object_name = 'films'
    template_name = 'simple_page/films.html'

class PoetryList(ListView):
    model = Poetry
    context_object_name = 'poetries'
    template_name = 'simple_page/poetries.html'

class VideoList(ListView):
    model = Video
    context_object_name = 'videos'
    template_name = 'simple_page/videos.html'

class NewsList(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'simple_page/news_list.html'

class NewsDetail(DetailView):
    model = News
    slug_field = 'slug'
    template_name = 'simple_page/news_detail.html'
