from django.db import models

# Create your models here.
class Bb(models.Model):
    login = models.TextField(null=True, blank=True)
    password = models.TextField(null=True, blank=True)



