from django.urls import path

from usuario.views.usuario import Usuario
from usuario.views.login import Login

urlpatterns = [
  path('', Login.to_login, name='tologin'),
  path('login/', Login.login, name='login'),
  path('login/cadastro/', Usuario.cadastro, name='cadastro'),
  path('login/esqueceu-senha/', Usuario.esqueceu_senha, name='esqueceu'),
  path('validacao/dados/', Usuario.is_usuario, name="is_usuario")
]