from django.urls import include, path
from .views import mention_query

urlpatterns = [
    path('mention/', mention_query, name='comments-mention-query'),
    path('', include('django_comments.urls')),
]
