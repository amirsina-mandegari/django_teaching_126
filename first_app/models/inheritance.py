from django.db import models


class CustomUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()


class Customer(CustomUser):
    address = models.TextField()


class Staff(CustomUser):
    role = models.CharField(max_length=50)
