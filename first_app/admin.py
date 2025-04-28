from django.contrib import admin

from first_app.models import BlogPost, Comment, PostAuthor

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(PostAuthor)
class PostAuthorAdmin(admin.ModelAdmin):
    pass