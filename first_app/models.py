from django.db import models


class PostAuthor(models.Model):
    first_name = models.TextField(null=False, blank=False)
    last_name = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BlogPost(models.Model):
    title = models.CharField(max_length=30, unique=True)
    content = models.TextField(null=True, blank=True)
    is_shown = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    authors = models.ManyToManyField(PostAuthor)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    
    def __str__(self):
        return f"{self.blog_post} {self.id}"
    

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    additional_data = models.CharField(max_length=100, null=True, blank=True)

