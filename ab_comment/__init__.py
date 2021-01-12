def get_model():
    from django_comments.models import Comment

    return Comment


def get_form():
    from .forms import CommentForm

    return CommentForm
