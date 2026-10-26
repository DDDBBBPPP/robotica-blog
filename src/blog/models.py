from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField('título', max_length=200)
    slug = models.SlugField('slug', max_length=220, unique=True)
    content = models.TextField('contenido', default='')
    excerpt = models.TextField('extracto', blank=True)
    author = models.CharField(
        'autoría',
        max_length=120,
        default='Autoría pendiente',
    )
    published_at = models.DateTimeField('fecha de publicación')
    is_published = models.BooleanField('publicado', default=False)

    class Meta:
        ordering = ('-published_at', '-pk')
        verbose_name = 'artículo'
        verbose_name_plural = 'artículos'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article-detail', kwargs={'slug': self.slug})


class AboutPage(models.Model):
    title = models.CharField('título', max_length=120, default='Sobre mí')
    content = models.TextField('presentación')
    updated_at = models.DateTimeField('actualizado', auto_now=True)

    class Meta:
        verbose_name = 'presentación del autor'
        verbose_name_plural = 'presentación del autor'

    def __str__(self):
        return self.title
