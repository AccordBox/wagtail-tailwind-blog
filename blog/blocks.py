#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-12-23 michael_yin
#

from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel,MultiFieldPanel, \
    InlinePanel, PageChooserPanel, StreamFieldPanel

class TwoColumnBlock(blocks.StructBlock):

    left_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
        ], icon='arrow-left', label='Left column content')

    right_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
        ], icon='arrow-right', label='Right column content')

    class Meta:
        template = 'blog/blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'

