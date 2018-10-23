# vim:sw=4 ts=4 et:
# Copyright (c) 2015 Torchbox Ltd.
# felicity@torchbox.com 2015-09-14
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely. This software is provided 'as-is', without any express or implied
# warranty.
#

from __future__ import absolute_import

from django import template

import markdown
import wagtailmd

register = template.Library()


@register.filter(name='markdown')
def markdown_filter(value):
    return markdown.markdown(
        value,
        extensions=[
            'toc',
            'extra',
            'codehilite',
            'wagtailmd.mdx.tables',
            'wagtailmd.mdx.mdx_mathjax',
        ],
        extension_configs={
            'codehilite': [
                ('css_class', "highlight")
            ]
        },
        output_format='html5'
    )
