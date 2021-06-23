from django.shortcuts import render, redirect
from django.http import HttpResponse

from usuario.models import Usuario as User

from .models import Cidade


def principal(request):
  
  if request.method == 'POST':
    
    dados = request.POST

    email = dados['email']

    password = dados['password']

    query_result = User.objects.filter(email=f"{email}", password=f"{password}")
    
    print(query_result)

    if len(query_result) > 0:
      
      request.session["email"] = email
      request.session["password"] = password
      print("AQUI")
      return render(request, 'cidades/principal.html', content_type='text/html')

  else:
    print("AQUI2")
    if (request.session.has_key("email")) and (request.session.has_key("password")):
      print("AQUI3")
      return render(request, 'cidades/principal.html')
    
    else:
      print("AQUI4")
      return redirect('/')

def tabela(request):

  if request.session.has_key("user"):
    userid = request.session["user"]   

    cidades = Cidade.objects.all()    
    
    return render(request, 'cidades/tabela.html', {"cidades": cidades})

  else:
    print("Nao tem id")
    return redirect('/')




def formlario(request):

  if request.session.has_key("user"):

    return render(request, 'cidades/formlario.html', { "CidadeTipo": FormIdCidadeTipo, 'bairro': FormIdBairro })

  else:
    print("Nao tem id")
    return redirect('/')

def updateData(request):
  data = request.POST
  
  print(data["idbairro"])


  
  Cidade.objects.filter(idBairro=data['idbairro']).update(
    idCidade=data['idcidade'],
    idTipo=data['idtipo'],
    idBairro=data['idbairro'],
    bairro=data['bairro']
  )

  return HttpResponse({"valor": True})


def deleteData(request):
  idBairro = request.POST["content"]
  
  Cidade.objects.filter(idBairro=f"{idBairro}").delete()


  return HttpResponse({"valor": True})

def insercaoData(request):
  return render(request, 'cidades/insercao.html', { "CidadeTipo": FormIdCidadeTipo, 'bairro': FormIdBairro })

def insertData(request):
  data = request.POST

  c = Cidade(    
    idCidade=data['idcidade'],
    idTipo=data['idtipo'],
    idBairro=data['idbairro'],
    bairro=data['bairro']
  )

  c.save()

  return HttpResponse({"valor": True})