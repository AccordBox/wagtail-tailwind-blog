import re

from django.dispatch import receiver
from django_comments.signals import comment_was_posted


@receiver(comment_was_posted)
def process_comment(sender, **kwargs):
    comment_instance = kwargs["comment"]
    comment_msg = comment_instance.comment

    mention_user_names = re.findall(r"@([^:\s]+)", comment_msg)
    print(f"user {mention_user_names} were just mentioned")
