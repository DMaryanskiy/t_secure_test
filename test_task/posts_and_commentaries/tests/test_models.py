"Модуль для тестирования моделей"

from django.test import TestCase

from ..models import Post, Comment, User


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username="auth")
        cls.post = Post.objects.create(
            author=cls.user,
            text="Тестовый пост"
        )
        cls.comment = Comment.objects.create(
            author=cls.user,
            post=cls.post,
            text="Тестовый коммент"
        )

    def test_models_have_correct_object_names(self):
        "Проверка корректности __str__"
        self.assertEqual(str(self.post), "Тестовый пост")
        self.assertEqual(str(self.comment), "Тестовый коммент")
