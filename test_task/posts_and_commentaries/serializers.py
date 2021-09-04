"Модуль, который содержит сериализаторы"
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    "Сериализатор постов"
    user = StringRelatedField()

    class Meta:
        "Мета-класс сериализатора с описанием модели и полей"
        model = Post
        fields = "__all__"
