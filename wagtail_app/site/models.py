import datetime
from django.db import models
from django.http import Http404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils.dateformat import DateFormat
from django.utils.formats import date_format
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.snippets.models import register_snippet
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.search import index
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtailcaptcha.models import WagtailCaptchaEmailForm
from wagtail.core.fields import StreamField, RichTextField
from django.utils.functional import cached_property

from taggit.models import Tag as TaggitTag
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from modelcluster.tags import ClusterTaggableManager
from wagtailmetadata.models import MetadataPageMixin
from django.db import models
from wagtail.contrib.settings.models import (
    BaseSiteSetting,
    register_setting,
)

from .blocks import BodyBlock


@register_setting
class SocialMediaSettings(BaseSiteSetting):
    facebook = models.URLField(blank=True, null=True)

class SitePage(RoutablePageMixin, Page):

    body = StreamField(BodyBlock(), blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("body")
    ]

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(WagtailCaptchaEmailForm, Page):
    thank_you_text = RichTextField(blank=True)

    body = StreamField(BodyBlock(), blank=True, use_json_field=True)
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("body"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text", classname="full"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address", classname="col6"),
                        FieldPanel("to_address", classname="col6"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Email Notification Config",
        ),
    ]
