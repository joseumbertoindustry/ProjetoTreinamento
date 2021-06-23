from django.shortcuts import render, redirect, HttpResponse

from usuario.models import Usuario as User

class Usuario:
  def cadastro(request):
    return render(request, 'usuario/cadastro.html')

  def esqueceu_senha(request):
    return render(request, 'usuario/esqueceu-senha.html')
  
  def is_usuario(request):
    dados = request.POST

    email = dados['email']

    password = dados['password']

    query_result = User.objects.filter(email=f"{email}", password=f"{password}")
    print(query_result, len(query_result))

    if len(query_result) > 0:
      
      request.session["email"] = email
      request.session["password"] = password
      return redirect("/cidades/principal/")
      #return render(request, "cidades/principal.html")
      
    else:
      return HttpResponse({"valido": False})
