from ..models import BlogCategory, Tag
from django.template import Library, loader
from urllib.parse import urlparse, urlunparse
from django.http import QueryDict
from wagtail_app.blog.utils import render_markdown

register = Library()

@register.filter(name='markdown')
def markdown(value):
    return render_markdown(value)
