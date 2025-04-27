from django.db import models


class PostAuthor(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()


class BlogPost(models.Model):
    title = models.CharField(max_length=30, unique=True)
    content = models.TextField(null=True, blank=True)
    is_shown = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    authors = models.ManyToManyField(PostAuthor)


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()