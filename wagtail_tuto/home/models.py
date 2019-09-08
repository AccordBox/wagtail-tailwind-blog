from django.db import models

from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                         StreamFieldPanel)
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock

from home.blocks import RowBlock


class HomePage(Page):
    pass


@register_setting
class CopyWritingSettings(BaseSetting):
    hero_title = models.CharField(
        max_length=255, help_text='Hero Header')
    hero_lead = RichTextField(
        max_length=255, help_text='Hero Lead Text')
    hero_cta_text = models.CharField(
        max_length=255, help_text='Hero CTA Text')
    hero_cta_url = models.URLField(
        max_length=255, help_text='Hero CTA Text')

    testimonial = StreamField([
        ('row', RowBlock()),
    ], null=True, blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('hero_title'),
                FieldPanel('hero_lead'),
                FieldPanel('hero_cta_text'),
                FieldPanel('hero_cta_url'),
            ],
            heading="Hero",
            classname="collapsible"
        ),
        StreamFieldPanel('testimonial'),
    ]
