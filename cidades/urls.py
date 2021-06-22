from django.urls import path

from . import views

urlpatterns = [
  path('esqueceu/', views.esqueceu, name='esqueceu'),
  path('principal/', views.principal, name='principal'),
  path('tabela/', views.tabela, name='tabela'),
  path('tabela/formlario/', views.formlario, name='formlario'),
  path('update/data/', views.updateData, name='Atualizacao'),
  path('delete/data/', views.deleteData, name='Delecao'),
  path('insercao/', views.insercaoData, name='Insercao'),
  path('insert/data/', views.insertData, name='Inseto')
]