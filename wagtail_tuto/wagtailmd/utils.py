from django.db.models import TextField
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.utils.widgets import WidgetWithScript


class MarkdownField(TextField):
    def __init__(self, **kwargs):
        super(MarkdownField, self).__init__(**kwargs)


class MarkdownPanel(FieldPanel):
    def __init__(self, field_name, classname="", widget=None, **kwargs):
        super(MarkdownPanel, self).__init__(
            field_name,
            classname=classname,
            widget=widget,
            **kwargs
        )

        if self.classname:
            if 'markdown' not in self.classname:
                self.classname += "markdown"
        else:
            self.classname = "markdown"
