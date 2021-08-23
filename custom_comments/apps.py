from django.apps import AppConfig


class CustomCommentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_comments'

    def ready(self):
        import custom_comments.receivers
