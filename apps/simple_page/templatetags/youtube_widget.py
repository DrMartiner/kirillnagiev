# -*- coding: utf-8 -*-

import re
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def youtube(url, name):
    regex = re.compile(r"^(http://)?(www\.)?(youtube\.com/watch\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})")
    match = regex.match(url)
    if not match: return ""
    video_id = match.group('id')
    return """
        <iframe width="439" height="267" src="http://www.youtube.com/embed/%s" frameborder="0" allowfullscreen></iframe>
        <figcaption>%s</figcaption>
        """ % (video_id, name)