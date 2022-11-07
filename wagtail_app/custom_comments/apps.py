from django.apps import AppConfig


class CustomCommentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wagtail_app.custom_comments'

    def ready(self):
        import wagtail_app.custom_comments.receivers
