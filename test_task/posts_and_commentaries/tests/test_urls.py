"Модуль для тестирования url-адресов"

from django.test import TestCase, Client

from ..models import Post, Comment, User


class StaticURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username="TestUser")
        cls.seconduser = User.objects.create_user(username="AnotherUser")

        cls.post = Post.objects.create(
            author=cls.user,
            text="Some text",
        )

        cls.comment = Comment.objects.create(
            author=cls.user,
            text="Some comment",
            post=cls.post,
        )

        cls.response = Comment.objects.create(
            author=cls.user,
            text="Some response",
            post=cls.post,
            prev_comment=cls.comment.id,
        )

    def setUp(self):
        self.guest_client = Client()

        self.owner = Client()
        self.owner.force_login(self.user)

        self.authorized_client = Client()
        self.authorized_client.force_login(self.seconduser)

    def test_register(self):
        "Проверка возможности зарегистрироваться"
        response = self.guest_client.post(
            "/api/v1/register",
            {
                "username": "register",
                "email": "barfoo@example.com",
                "password": "kinda_weird_password1",
            }
        )
        self.assertEqual(response.status_code, 201)
        response = self.guest_client.post(
            "/api/v1/register",
            {
                "username": "register@ex.com",
                "email": "barfoo",
                "password": "kinda_weird_password1",
            }
        )
        self.assertEqual(response.status_code, 400)

    def test_pages_unauthorized(self):
        "Проверка доступности страниц для неавторизованного пользователя"
        pages_codes = {
            "/api/v1/": 200,
            f"/api/v1/{self.post.id}": 200,
            "/api/v1/create": 403,
            f"/api/v1/{self.post.id}/create": 403,
            f"/api/v1/{self.post.id}/{self.comment.id}": 200,
            f"/api/v1/{self.post.id}/{self.comment.id}/create": 403
        }
        for address, code in pages_codes.items():
            with self.subTest(address=address):
                response = self.guest_client.get(address)
                self.assertEqual(response.status_code, code)

    def test_editing_unauthorized_and_not_owner(self):
        """
        Проверка возможности редактирования и удаления объекта
        неавторизованным пользователем и не создателем этого обьекта.
        """
        pages_codes = {
            f"/api/v1/{self.post.id}/{self.comment.id}": 403,
            f"/api/v1/{self.post.id}": 403,
        }
        for address, code in pages_codes.items():
            with self.subTest(address=address):
                response = self.guest_client.put(address)
                self.assertEqual(response.status_code, code)
                response = self.authorized_client.put(address)
                self.assertEqual(response.status_code, code)
                response = self.guest_client.delete(address)
                self.assertEqual(response.status_code, code)
                response = self.authorized_client.delete(address)
                self.assertEqual(response.status_code, code)

    def test_editing_owner(self):
        """
        Проверка возможности редактирования и удаления объекта
        его создателем.
        """
        pages_codes = {
            f"/api/v1/{self.post.id}/{self.comment.id}": [200, 204, 400],
            f"/api/v1/{self.post.id}": [200, 204, 400],
        }
        for address, code in pages_codes.items():
            with self.subTest(address=address):
                response = self.owner.put(
                    address,
                    {
                        "text": "New text"
                    },
                    content_type='application/json'
                )
                self.assertEqual(response.status_code, code[0])
                response = self.owner.put(address)
                self.assertEqual(response.status_code, code[2])
                response = self.owner.delete(address)
                self.assertEqual(response.status_code, code[1])

    def test_creating(self):
        "Проверка возможности создания объекта"
        pages_codes = {
            "/api/v1/create": [201, 400],
            f"/api/v1/{self.post.id}/create": [201, 400],
            f"/api/v1/{self.post.id}/{self.comment.id}/create": [201, 400],
        }
        for address, code in pages_codes.items():
            with self.subTest(address=address):
                response = self.authorized_client.post(
                    address,
                    {
                        "text": "I've created new object"
                    }
                )
                self.assertEqual(response.status_code, code[0])
                response = self.authorized_client.post(address)
                self.assertEqual(response.status_code, code[1])
