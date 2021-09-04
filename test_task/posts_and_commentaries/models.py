"Модуль, описывающий модели БД"
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    "Модель постов с полями текст, автор и дата публикации"
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_post")

    def __str__(self):
        return self.text

class Comment(models.Model):
    """
    Модель комментариев с полями текст, автор, дата публикации,
    соответствующим постом и родительским комментарием
    """
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")
    prev_comment = models.PositiveIntegerField(default=0)
