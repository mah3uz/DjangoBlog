from django.contrib import admin

from blog_post.models import BlogPost, Categories


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')

make_published.short_description = "Mark selected stories as published"

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status']
    list_filter = ['created_at']
    search_fields = ['title', 'body']
    ordering = ['-created_at']
    actions = [make_published]

    class Meta:
        model = BlogPost

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Categories)
