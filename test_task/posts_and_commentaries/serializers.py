"Модуль, который содержит сериализаторы"
from django.contrib import auth
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from .models import Post, User, Comment

class PostSerializer(serializers.ModelSerializer):
    "Сериализатор постов"
    author = StringRelatedField()

    class Meta:
        "Мета-класс сериализатора с описанием модели и полей"
        model = Post
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    "Сериализатор пользователей"
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user

    class Meta:
        "Мета-класс сериализатора с описанием модели и полей"
        model = User
        fields = ("id", "username", "email", "password")

class CommentSerializer(serializers.ModelSerializer):
    "Сериализатор комментариев"
    author = StringRelatedField()
    post = StringRelatedField()
    comment = StringRelatedField()

    class Meta:
        "Мета-класс сериализатора с описанием модели и полей"
        model = Comment
        fields = "__all__"
