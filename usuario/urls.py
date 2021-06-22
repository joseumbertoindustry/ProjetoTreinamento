from django.urls import path

from . import views

urlpatterns = [
  path('', views.to_login, name='tologin'),
  path('login/', views.login, name='login'),
  path('login/cadastro/', views.cadastro, name='cadastro'),
  path('login/esqueceu-senha/', views.esqueceu_senha, name='esqueceu')
]