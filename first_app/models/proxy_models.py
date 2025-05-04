from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    def display_title(self):
        return f"published book!!!!: {self.title}"


class PublishedBook(Book):    
    class Meta:
        proxy = True

    def display_title(self):
        return f"published book: {self.title}"
