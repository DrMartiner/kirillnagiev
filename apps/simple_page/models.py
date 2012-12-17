# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models

class Film(models.Model):
    name = models.CharField('Название', max_length=64)
    num = models.PositiveIntegerField('Порядок вывода', default=0, blank=True, null=True,
        help_text='Чем больше, тем выше в списке'
    )
    role = models.CharField('Роль', max_length=64, blank=True, null=True)
    year = models.PositiveSmallIntegerField('Год', blank=True, null=True)
    producer = models.CharField('Режиссёр', max_length=64, blank=True, null=True)
    image = models.ImageField('Обложка', blank=True, null=True,
        upload_to='films_covert', default='img/film_covert.jpg',
        help_text='Соотношение 2:3. Масштабироватсья будет до размеров 45x65 px'
    )
    link = models.URLField('Ссылка на фильм', verify_exists=False, blank=True, null=True)

    class Meta:
        ordering = ('-num', )
        verbose_name = 'Фимльм'
        verbose_name_plural = 'Фильмы'

class Poetry(models.Model):
    name = models.CharField('Название', max_length=64)
    num = models.PositiveIntegerField('Порядок вывода', default=0, blank=True, null=True,
        help_text='Чем больше, тем выше в списке'
    )
    year = models.PositiveSmallIntegerField('Год', blank=True, null=True)
    contetn = models.TextField('Стих')

    class Meta:
        ordering = ('-num', )
        verbose_name = 'Стих'
        verbose_name_plural = 'Стихи'

class Video(models.Model):
    name = models.CharField('Заголовок', max_length=64)
    num = models.PositiveIntegerField('Порядок вывода', default=0, blank=True, null=True,
        help_text='Чем больше, тем выше в списке'
    )
    link = models.URLField('Ссылка на YouTube', verify_exists=False,
        help_text='Например: http://www.youtube.com/watch?v=3nbKqgpVADk'
    )

    class Meta:
        ordering = ('-num', )
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Видео'

class News(models.Model):
    name = models.CharField('Заголовок', max_length=64)
    num = models.PositiveIntegerField('Порядок вывода', default=0, blank=True, null=True,
        help_text='Чем больше, тем выше в списке'
    )
    slug = models.SlugField('Заголовок транслитом', unique=True)
    contetn = models.TextField('Новость')
    link = models.URLField('Ссылка на новость', verify_exists=False, blank=True, null=True)
    pub_date = models.DateField('Опубликовано', default=datetime.today)

    class Meta:
        ordering = ('-num', '-pub_date')
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Photo(models.Model):
    image = models.ImageField('Изображение', upload_to='photos')
    num = models.PositiveIntegerField('Порядок вывода', default=0, blank=True, null=True,
        help_text='Чем больше, тем выше в списке'
    )
    alt = models.CharField('Подсказка', max_length=64, blank=True, null=True, help_text='Полезно для СЕО')

    class Meta:
        ordering = ('-num', )
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
