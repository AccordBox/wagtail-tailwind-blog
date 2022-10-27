import emoji
from django.template import Library, loader

register = Library()


@register.filter(name="comment_post_processor")
def comment_post_processor(value):
    return emoji.emojize(value, language="alias")
