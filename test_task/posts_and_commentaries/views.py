"Модуль, который содержит все дженерики"
from rest_framework import generics, permissions
from .serializers import PostSerializer, UserSerializer
from .models import Post, User

class PostListAPI(generics.ListAPIView):
    "Класс, выводящий список всех постов"
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateAPI(generics.CreateAPIView):
    "Класс, создающий новую запись в таблице Post"
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

class PostUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    Класс, отображающий конкретный пост.
    С помощью этой функции можно изменить запись и удалить ее.
    """
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

class UserCreateView(generics.CreateAPIView):
    "Класс, создающий пользователя"
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
