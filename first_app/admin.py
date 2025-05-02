from django.contrib import admin

from first_app.models import BlogPost, Comment, PostAuthor

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title', 'is_shown', 'created_at')
    list_filter=('is_shown','title')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('id', 'blog_post', 'author')
    search_fields=('blog_post__title','author')
    raw_id_fields = ('blog_post',)

@admin.register(PostAuthor)
class PostAuthorAdmin(admin.ModelAdmin):
    pass