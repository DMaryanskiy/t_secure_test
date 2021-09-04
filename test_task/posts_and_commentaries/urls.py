"Модуль, который содержит url-адреса функций внутри приложения"
from django.urls import path

from .views import (
    PostListAPI,
    PostCreateAPI,
    PostUpdateDeleteAPI,
    UserCreateView
)

urlpatterns = [
    path("", PostListAPI.as_view()),
    path("<int:pk>", PostUpdateDeleteAPI.as_view()),
    path("create", PostCreateAPI.as_view()),
    path("register", UserCreateView.as_view()),
]
