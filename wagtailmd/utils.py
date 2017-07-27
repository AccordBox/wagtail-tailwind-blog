from django.db.models import TextField
from django.utils.translation import ugettext_lazy as _

from wagtail.utils.widgets import WidgetWithScript
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class MarkdownField(TextField):
    def __init__(self, **kwargs):
        super(MarkdownField, self).__init__(**kwargs)

class MarkdownPanel(FieldPanel):
    def __init__(self, field_name, classname="", widget=None):
        super(MarkdownPanel, self).__init__(field_name, classname, None)

        if self.classname != "":
            self.classname += " "
        self.classname += "markdown"


