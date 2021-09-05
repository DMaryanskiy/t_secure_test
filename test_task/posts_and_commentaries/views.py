"Модуль, который содержит все дженерики"
from rest_framework import generics, permissions

from django.shortcuts import get_object_or_404
from .serializers import CommentSerializer, PostSerializer, UserSerializer
from .models import Post, User, Comment
from .permissions import IsOwnerOrReadOnly


class PostListAPI(generics.ListAPIView):
    "Класс для вывода списка всех постов"
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateAPI(generics.CreateAPIView):
    "Класс для создания новой записи в таблице Post"
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class PostUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    Класс для отображения конкретного поста.
    С помощью этой функции можно изменить запись и удалить ее.
    """
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        return serializer.save(author=self.request.user)


class UserCreateView(generics.CreateAPIView):
    "Класс для создания пользователя"
    model = User
    serializer_class = UserSerializer


class CommentCreateAPI(generics.CreateAPIView):
    "Класс для создания комментариев"
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        if self.kwargs.get("comment_id"):
            return serializer.save(
                author=self.request.user,
                post=get_object_or_404(Post, pk=self.kwargs.get("pk")),
                prev_comment=get_object_or_404(Comment, pk=self.kwargs.get("comment_id")).pk
            )
        return serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=self.kwargs.get("pk")),
        )


class CommentRetrieveAPI(generics.RetrieveUpdateDestroyAPIView):
    "Класс для просмотра, обновления и удаления комментария"
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        return Comment.objects.filter(post=post)

    def perform_update(self, serializer):
        return serializer.save(author=self.request.user)
