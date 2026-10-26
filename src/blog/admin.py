from django.contrib import admin

from .models import AboutPage, Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'is_published')
    list_filter = ('is_published', 'published_at')
    search_fields = ('title', 'content', 'excerpt', 'author')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    fieldsets = (
        ('Contenido', {'fields': ('title', 'slug', 'excerpt', 'content')}),
        ('Publicación', {'fields': ('author', 'published_at', 'is_published')}),
    )


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title', 'content')

    def has_add_permission(self, request):
        return not AboutPage.objects.exists()
