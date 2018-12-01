from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from .models import Portfolio


class PortfolioTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_user',
            email='test@email.com',
            password='test_user'
        )

        self.portfolio = Portfolio.objects.create(
            title='Test Portfolio',
            slug='test-portfolio',
            author=self.user,
            status='published',
            published_at=timezone.now(),
            created_at=timezone.now(),
            updated_at=timezone.now(),
            thumbnail_image='django.png',
            description='Description',
            contents='Contents',
            portfolio_tag='test'
        )

    def test_portfolio_content(self):
        self.assertEqual(f'{self.portfolio.title}', 'Test Portfolio')
        self.assertEqual(f'{self.portfolio.slug}', 'test-portfolio')
        self.assertEqual(f'{self.portfolio.author}', 'test_user')
        self.assertEqual(f'{self.portfolio.status}', 'published')
        self.assertEqual(f'{self.portfolio.thumbnail_image}', 'django.png')
        self.assertEqual(f'{self.portfolio.description}', 'Description')
        self.assertEqual(f'{self.portfolio.contents}', 'Contents')
        self.assertEqual(f'{self.portfolio.portfolio_tag}', 'test')

    def test_portfolio_list_view(self):
        response = self.client.get(reverse('portfolio_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Description')
        self.assertContains(response, 'Contents')
        self.assertTemplateUsed(response, 'portfolio_list.html')

    def test_portfolio_detail_view(self):
        response = self.client.get('/portfolio/test-portfolio/')
        no_response = self.client.get('/portfolio/no-exist/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test Portfolio')
        self.assertTemplateUsed(response, 'portfolio_detail.html')