from django.db import models
from django.contrib.auth.models import User
from userapp.models import Foydalanuvchi


class Maqola(models.Model):
    sarlavha = models.CharField(max_length=100)
    mavzu = models.CharField(max_length=30,null=True,blank=True)
    sana = models.DateField()
    matn = models.TextField()
    muallif = models.ForeignKey(Foydalanuvchi,on_delete=models.SET_NULL, null=True)






