from django.db import models
from django.utils import timezone

class PostAuthor(models.Model):
    first_name = models.TextField(null=False, blank=False)
    last_name = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class BlogPostQueryset(models.QuerySet):
    def filter_shown(self, **kwargs):
        return self.filter(is_shown=True, **kwargs)
    
    def delete(self, hard_delete=False):
        if hard_delete is True:
            return super().delete()
        return self.update(removed_at=timezone.now())
    
    def filter_active(self, **kwargs):
        return self.filter(removed_at__isnull=True, **kwargs)


class BlogPost(models.Model):
    title = models.CharField(max_length=30, unique=True)
    content = models.TextField(null=True, blank=True)
    is_shown = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    authors = models.ManyToManyField(PostAuthor)
    removed_at = models.DateTimeField(null=True, blank=True)

    objects = BlogPostQueryset.as_manager()

    class Meta:
        permissions = [
            ('can_publish', 'can publish blog post'),
            ('can_archive', 'can archive blog post')
        ]

    def __str__(self):
        return f"{self.title}"
    
    def delete(self, hard_delete=False, *args, **kwargs):
        if hard_delete is True:
            return super().delete(*args, **kwargs)
        self.removed_at = timezone.now()
        self.save()


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

    class Meta:
        permissions = [
            ('send_contact_us', 'can send contact us')
        ]
