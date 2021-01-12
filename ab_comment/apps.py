from django.apps import AppConfig


class AbCommentConfig(AppConfig):
    name = 'ab_comment'

    def ready(self):
        import ab_comment.receivers
