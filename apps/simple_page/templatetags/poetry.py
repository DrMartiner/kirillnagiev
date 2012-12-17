# -*- coding: utf-8 -*-

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def line_count(poetry):
    try:
        return len(poetry.split('\n'))
    except Exception:
        return 0
