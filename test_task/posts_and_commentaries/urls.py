"Модуль, который содержит url-адреса функций внутри приложения"
from django.urls import path

from .views import (
    PostListAPI,
    PostCreateAPI,
    PostUpdateDeleteAPI,
    UserCreateView,
    CommentCreateAPI,
    CommentRetrieveAPI,
)

urlpatterns = [
    path("", PostListAPI.as_view()),
    path("<int:pk>", PostUpdateDeleteAPI.as_view()),
    path("create", PostCreateAPI.as_view()),
    path("register", UserCreateView.as_view()),
    path("<int:pk>/create", CommentCreateAPI.as_view()),
    path("<int:post_id>/<int:pk>", CommentRetrieveAPI.as_view()),
    path("<int:pk>/<int:comment_id>/create", CommentCreateAPI.as_view())
]
