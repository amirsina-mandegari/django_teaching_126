from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    manager_name = models.CharField(max_length=10)
    age = models.PositiveIntegerField()