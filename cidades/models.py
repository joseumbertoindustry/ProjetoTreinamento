from django.db import models

class Cidade(models.Model):
  idCidade = models.IntegerField()
  idTipo = models.IntegerField()
  idBairro = models.IntegerField()
  bairro = models.CharField(max_length=50)
