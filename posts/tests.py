from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="Привет", text="Пока", url="Привет", user=1)
        Post.objects.create(title="Круто всё!", text="Но есть проблемы", url="Круто всё!", user=2)

    def test_posts_titles(self):
        post1 = Post.objects.get(title="Привет")
        post2 = Post.objects.get(title="Круто всё!")
        self.assertEqual(post1.get_comment(), 'Привет')
        self.assertEqual(post2.get_comment(), 'Круто всё!')