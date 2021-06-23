from django.db import models
from django.db.models.fields import CharField

class Usuario(models.Model):
  nome = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)
  password = models.CharField(max_length=100)
