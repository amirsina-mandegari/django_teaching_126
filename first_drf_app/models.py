from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    manager_name = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    employees = models.ManyToManyField(Employee)

    @property
    def age_in_month(self):
        return self.age * 12