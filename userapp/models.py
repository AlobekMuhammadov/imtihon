from django.db import models
from django.contrib.auth.models import User


class Foydalanuvchi(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.SmallIntegerField(default=18)
    kasb = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism




