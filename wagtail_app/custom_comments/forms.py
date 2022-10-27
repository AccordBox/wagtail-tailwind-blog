from django import forms
from django.conf import settings
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.utils.encoding import force_str
from django_comments.forms import CommentDetailsForm
from captcha.fields import ReCaptchaField

username_validator = UnicodeUsernameValidator()



class CommentForm(CommentDetailsForm):
    name = forms.CharField(
        label="UserName", max_length=50, validators=[username_validator]
    )
    captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields.pop("url")

    def get_comment_create_data(self, site_id=None):
        return dict(
            content_type=ContentType.objects.get_for_model(self.target_object),
            object_pk=force_str(self.target_object._get_pk_val()),
            user_name=self.cleaned_data["name"],
            user_email=self.cleaned_data["email"],
            comment=self.cleaned_data["comment"],
            submit_date=timezone.now(),
            site_id=site_id or getattr(settings, "SITE_ID", None),
            is_public=True,
            is_removed=False,
        )

    def get_content_type(self):
        return str(self.target_object._meta)

    def get_object_pk(self):
        return str(self.target_object._get_pk_val())
