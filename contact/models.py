from django.db import models

# Create your models here.


class Contact(models.Model):
    fullmame = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    pho = models.CharField(max_length=10)
