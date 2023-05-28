from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Blog, Post, Category

class MyPostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.blog = Blog.objects.create(
            name='Test Blog',
            description='This is a test blog',
            author=self.user
        )
        self.category = Category.objects.create(
            category='Test Category',
            blog=self.blog
        )
        self.post = Post.objects.create(
            title='Test Post',
            body='This is a test post',
            blog=self.blog
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 200)

        data = {
            'title': 'New Post',
            'body': 'This is a new post',
            'blog': self.blog.pk
        }
        response = self.client.post(reverse('post_create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.get(pk=2).title, 'New Post')

    def test_post_update_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post_update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)

        data = {
            'title': 'Updated Post',
            'body': 'This is an updated post',
            'blog': self.blog.pk
        }
        response = self.client.post(reverse('post_update', args=[self.post.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Post')

    def test_post_delete_view(self):
        response = self.client.get(reverse('post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)

        self.assertEqual(Post.objects.count(), 1)

        response = self.client.post(reverse('post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)

        self.assertEqual(Post.objects.count(), 0)

