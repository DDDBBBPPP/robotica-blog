from datetime import timedelta

from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model

from .models import AboutPage, Article


class HomePageTests(TestCase):
    def setUp(self):
        now = timezone.now()
        self.old_article = Article.objects.create(
            title='Artículo antiguo',
            slug='articulo-antiguo',
            excerpt='Extracto antiguo.',
            content='Contenido antiguo.',
            author='Autora antigua',
            published_at=now - timedelta(days=1),
            is_published=True,
        )
        self.recent_article = Article.objects.create(
            title='Artículo reciente',
            slug='articulo-reciente',
            excerpt='Extracto reciente.',
            content='Contenido reciente.',
            author='Autor reciente',
            published_at=now,
            is_published=True,
        )

    def test_home_returns_success_and_displays_blog_name(self):
        response = self.client.get(reverse('blog:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Robótica')
        self.assertContains(response, 'Artículos recientes')
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_home_lists_published_articles_newest_first_with_metadata_and_links(self):
        response = self.client.get(reverse('blog:home'))
        content = response.content.decode()

        self.assertLess(
            content.index(self.recent_article.title),
            content.index(self.old_article.title),
        )
        self.assertContains(response, self.recent_article.excerpt)
        self.assertContains(response, self.old_article.excerpt)
        self.assertContains(response, self.recent_article.author)
        self.assertContains(
            response,
            f'href="{self.recent_article.get_absolute_url()}"',
        )
        self.assertContains(
            response,
            f'href="{self.old_article.get_absolute_url()}"',
        )

    def test_article_link_opens_published_article(self):
        response = self.client.get(self.recent_article.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recent_article.title)
        self.assertContains(response, self.recent_article.author)
        self.assertContains(response, self.recent_article.content)

    def test_home_excludes_unpublished_articles(self):
        Article.objects.create(
            title='Borrador',
            slug='borrador',
            excerpt='Extracto privado.',
            content='Contenido privado.',
            author='Editor',
            published_at=timezone.now(),
            is_published=False,
        )

        response = self.client.get(reverse('blog:home'))

        self.assertNotContains(response, 'Borrador')
        self.assertNotContains(response, 'Extracto privado.')

    def test_home_shows_message_when_there_are_no_published_articles(self):
        Article.objects.update(is_published=False)

        response = self.client.get(reverse('blog:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Todavía no hay artículos publicados.')

    def test_unpublished_article_returns_404(self):
        unpublished = Article.objects.create(
            title='No publicado',
            slug='no-publicado',
            excerpt='Extracto privado.',
            content='Contenido privado.',
            author='Editor',
            published_at=timezone.now(),
            is_published=False,
        )

        response = self.client.get(unpublished.get_absolute_url())

        self.assertEqual(response.status_code, 404)

    def test_missing_article_returns_404(self):
        response = self.client.get('/articulos/no-existe/')

        self.assertEqual(response.status_code, 404)

    def test_article_content_preserves_paragraphs_and_subheadings(self):
        article = Article.objects.create(
            title='Estructura de un robot',
            slug='estructura-de-un-robot',
            excerpt='Cómo se estructura un robot.',
            content='## Sensores\n\nLos sensores permiten percibir el entorno.',
            author='Autora',
            published_at=timezone.now(),
            is_published=True,
        )

        response = self.client.get(article.get_absolute_url())

        self.assertContains(response, '<h2>Sensores</h2>', html=True)
        self.assertContains(
            response,
            '<p>Los sensores permiten percibir el entorno.</p>',
            html=True,
        )

    @override_settings(DEBUG=False)
    def test_missing_article_uses_not_found_page(self):
        response = self.client.get('/articulos/no-existe/')

        self.assertEqual(response.status_code, 404)
        self.assertContains(response, 'Página no encontrada', status_code=404)


class AboutPageTests(TestCase):
    def setUp(self):
        self.about_page = AboutPage.objects.create(
            content='## Quién soy\n\nUna presentación sobre robótica.'
        )

    def test_about_page_is_public_and_identifiable(self):
        response = self.client.get(reverse('blog:about'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sobre mí')
        self.assertContains(response, 'Una presentación sobre robótica.')
        self.assertContains(response, 'href="/sobre-mi/"')

    def test_main_navigation_links_to_about_page(self):
        response = self.client.get(reverse('blog:home'))

        self.assertContains(response, 'href="/sobre-mi/"')
        self.assertContains(response, 'Sobre mí')

    def test_about_page_can_be_updated(self):
        self.about_page.content = 'Presentación actualizada.'
        self.about_page.save()

        response = self.client.get(reverse('blog:about'))

        self.assertContains(response, 'Presentación actualizada.')


class ArticleAdminTests(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.admin = user_model.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='secret-password',
        )

    def test_admin_requires_authentication(self):
        response = self.client.get('/admin/blog/article/')

        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin/login/', response.url)

    def test_non_staff_user_cannot_access_admin(self):
        user = get_user_model().objects.create_user(
            username='reader',
            password='reader-password',
        )
        self.client.force_login(user)

        response = self.client.get('/admin/')

        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin/login/', response.url)

    def test_staff_user_without_model_permissions_cannot_manage_articles(self):
        user = get_user_model().objects.create_user(
            username='staff',
            password='staff-password',
            is_staff=True,
        )
        self.client.force_login(user)

        response = self.client.get('/admin/blog/article/')

        self.assertEqual(response.status_code, 403)

    def test_authenticated_editor_can_access_article_admin(self):
        self.client.force_login(self.admin)

        response = self.client.get('/admin/blog/article/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Seleccione artículo a modificar')

    def test_authenticated_editor_can_open_article_form(self):
        self.client.force_login(self.admin)

        response = self.client.get('/admin/blog/article/add/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id_title')
        self.assertContains(response, 'id_author')
        self.assertContains(response, 'id_is_published')

    def test_authenticated_editor_can_access_about_admin(self):
        self.client.force_login(self.admin)

        response = self.client.get('/admin/blog/aboutpage/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'presentación del autor')

    def test_editor_can_publish_and_unpublish_an_article(self):
        self.client.force_login(self.admin)
        article = Article.objects.create(
            title='Ciclo editorial',
            slug='ciclo-editorial',
            excerpt='Extracto editorial.',
            content='Contenido editorial.',
            author='Editor',
            published_at=timezone.now(),
        )

        self.assertEqual(
            self.client.get(article.get_absolute_url()).status_code,
            404,
        )

        article.is_published = True
        article.save()
        self.assertEqual(
            self.client.get(article.get_absolute_url()).status_code,
            200,
        )

        article.is_published = False
        article.save()
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(response.status_code, 404)
        self.assertNotContains(response, article.title, status_code=404)
