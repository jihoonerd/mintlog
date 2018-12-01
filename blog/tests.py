from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_user',
            email='test@email.com',
            password='test_user'
        )

        self.post = Post.objects.create(
            title='Test Posting',
            slug='test-posting',
            author=self.user,
            status='published',
            published_at=timezone.now(),
            created_at=timezone.now(),
            updated_at=timezone.now(),
            thumbnail_image='django.png',
            description='Description',
            contents='Contents',
            post_tag='test'
        )

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Test Posting')
        self.assertEqual(f'{self.post.slug}', 'test-posting')
        self.assertEqual(f'{self.post.author}', 'test_user')
        self.assertEqual(f'{self.post.status}', 'published')
        self.assertEqual(f'{self.post.thumbnail_image}', 'django.png')
        self.assertEqual(f'{self.post.description}', 'Description')
        self.assertEqual(f'{self.post.contents}', 'Contents')
        self.assertEqual(f'{self.post.post_tag}', 'test')

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Description')
        self.assertContains(response, 'Contents')
        self.assertTemplateUsed(response, 'post_list.html')

    def test_post_detail_view(self):
        response = self.client.get('/blog/test-posting/')
        no_response = self.client.get('/blog/no-exist/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test Posting')
        self.assertTemplateUsed(response, 'post_detail.html')