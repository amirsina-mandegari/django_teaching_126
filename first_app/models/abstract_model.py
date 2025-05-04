from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserLogin(TimeStampModel):
    username = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
