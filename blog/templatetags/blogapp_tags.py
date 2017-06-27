# -*- coding: utf-8 -*-
from django.template import Library, loader
from django.core.urlresolvers import resolve

from ..urls import get_entry_url, get_feeds_url
from ..models import Category, Tag

register = Library()

@register.simple_tag(takes_context=True)
def entry_url(context, entry, blog_page):
    import ipdb; ipdb.set_trace()
    return get_entry_url(entry, blog_page.page_ptr, context['request'].site.root_page)


