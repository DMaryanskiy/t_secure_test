"Модуль, который содержит сериализаторы"
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from .models import Post, User

class PostSerializer(serializers.ModelSerializer):
    "Сериализатор постов"
    user = StringRelatedField()

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
