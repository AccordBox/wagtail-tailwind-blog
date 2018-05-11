# -*- coding: utf-8 -*-
import six

from django.template import Library, loader
from django.urls import resolve

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

@register.inclusion_tag('blog/comments/disqus.html', takes_context=True)
def show_comments(context):
    blog_page = context['blog_page']
    post = context['post']
    path = post_date_url(post, blog_page)

    raw_url = context['request'].get_raw_uri()
    parse_result = six.moves.urllib.parse.urlparse(raw_url)
    abs_path = six.moves.urllib.parse.urlunparse([
        parse_result.scheme,
        parse_result.netloc,
        path,
        "",
        "",
        ""
    ])

    return {'disqus_url': abs_path,
            'disqus_identifier': post.pk,
            'request': context['request']}

@register.simple_tag(takes_context=True)
def canonical_url(context, post=None):
    if post and resolve(context.request.path_info).url_name == 'wagtail_serve':
        return context.request.build_absolute_uri(post_date_url(post, post.blog_page))
    return context.request.build_absolute_uri()

