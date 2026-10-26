from django.db import migrations, models
from django.utils import timezone


def create_initial_content(apps, schema_editor):
    Article = apps.get_model('blog', 'Article')
    AboutPage = apps.get_model('blog', 'AboutPage')

    AboutPage.objects.get_or_create(
        title='Sobre mí',
        defaults={
            'content': (
                'Escribo sobre robótica, automatización y las ideas que '
                'conectan la tecnología con nuestra vida cotidiana.'
            ),
        },
    )
    Article.objects.get_or_create(
        slug='primeros-pasos-en-robotica',
        defaults={
            'title': 'Primeros pasos en robótica',
            'content': (
                '## Qué es la robótica\n\n'
                'La robótica reúne ingeniería, programación y diseño para '
                'crear máquinas capaces de percibir y actuar.\n\n'
                '## Una mirada práctica\n\n'
                'En este blog exploraremos sus conceptos y aplicaciones '
                'con una mirada clara y accesible.'
            ),
            'excerpt': (
                'Una introducción a los conceptos que forman la robótica '
                'moderna.'
            ),
            'author': 'Autoría del blog',
            'published_at': timezone.now(),
            'is_published': True,
        },
    )


def remove_initial_content(apps, schema_editor):
    Article = apps.get_model('blog', 'Article')
    AboutPage = apps.get_model('blog', 'AboutPage')
    Article.objects.filter(slug='primeros-pasos-en-robotica').delete()
    AboutPage.objects.filter(title='Sobre mí').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_article_author_alter_article_excerpt'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'title',
                    models.CharField(
                        default='Sobre mí',
                        max_length=120,
                        verbose_name='título',
                    ),
                ),
                ('content', models.TextField(verbose_name='presentación')),
                (
                    'updated_at',
                    models.DateTimeField(
                        auto_now=True,
                        verbose_name='actualizado',
                    ),
                ),
            ],
            options={
                'verbose_name': 'presentación del autor',
                'verbose_name_plural': 'presentación del autor',
            },
        ),
        migrations.RunPython(create_initial_content, remove_initial_content),
    ]
