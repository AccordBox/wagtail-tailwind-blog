# -*- coding: utf-8 -*-
from django.template import Library, loader
from django.core.urlresolvers import resolve

from ..models import BlogCategory as Category, Tag

register = Library()

@register.simple_tag()
def post_date_url(post, blog_page):
    post_date = post.date
    url = blog_page.url + blog_page.reverse_subpage(
        'post_by_date_slug',
        args=(
            post_date.year,
            '{0:02}'.format(post_date.month),
            '{0:02}'.format(post_date.day),
            post.slug,
        )
    )
    return url

@register.inclusion_tag('blog/components/tags_list.html', takes_context=True)
def tags_list(context, limit=None):
    blog_page = context['blog_page']
    tags = Tag.objects.all()
    if limit:
        tags = tags[:limit]
    return {'blog_page': blog_page, 'request': context['request'], 'tags': tags}


@register.inclusion_tag('blog/components/categories_list.html', takes_context=True)
def categories_list(context):
    blog_page = context['blog_page']
    categories = Category.objects.all()
    return {'blog_page': blog_page, 'request': context['request'], 'categories': categories}


@register.inclusion_tag('blog/components/post_categories_list.html', takes_context=True)
def post_categories(context):
    blog_page = context['blog_page']
    post = context['post']
    post_categories = post.categories.all()
    return {'blog_page': blog_page, 'post_categories': post_categories, 'request': context['request']}


@register.inclusion_tag('blog/components/post_tags_list.html', takes_context=True)
def post_tags_list(context):
    blog_page = context['blog_page']
    post = context['post']

    post_tags = post.tags.all()

    return {'blog_page': blog_page, 'request': context['request'], 'post_tags': post_tags}
