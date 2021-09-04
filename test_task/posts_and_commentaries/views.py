"Модуль, который содержит все viewsets"
from rest_framework import generics

from .serializers import PostSerializer
from .models import Post

class PostListAPI(generics.ListAPIView):
    "Класс, выводящий список всех постов"
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateAPI(generics.CreateAPIView):
    "Класс, создающий новую запись в таблице Post"
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    Класс, отображающий конкретный пост.
    С помощью этой функции можно изменить запись и удалить ее.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
