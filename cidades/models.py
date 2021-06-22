from django.db import models

class User(models.Model):
  email = models.CharField(max_length=200)
  senha = models.CharField(max_length=200)

class Cidade(models.Model):
  idCidade = models.IntegerField()
  idTipo = models.IntegerField()
  idBairro = models.IntegerField()
  bairro = models.CharField(max_length=50)


'''
Id Da cidade | IdCIdade
Id tipo | IdTipo
Id do bairro | IdBairro
nome do bairro | bairro
'''