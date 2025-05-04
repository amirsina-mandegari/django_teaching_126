from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()


class Customer(User):
    address = models.TextField()


class Staff(User):
    role = models.CharField(max_length=50)
