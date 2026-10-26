from django.shortcuts import get_object_or_404, render

from .models import AboutPage, Article


def home(request):
    articles = Article.objects.filter(is_published=True)
    return render(request, 'blog/home.html', {'articles': articles})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    return render(request, 'blog/article_detail.html', {'article': article})


def about(request):
    about_page = AboutPage.objects.order_by('-updated_at').first()
    return render(request, 'blog/about.html', {'about_page': about_page})
