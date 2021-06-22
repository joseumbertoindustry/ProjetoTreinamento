from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms.login import FormLogin, FormIdCidadeTipo, FormIdBairro
from .models import User, Cidade

def login(request):  
  return render(request, 'cidades/login.html', { "form": FormLogin })



def esqueceu(request):
  
  return render(request, 'cidades/esqueceu.html')


def principal(request):
  if request.method == 'POST':
    
    form = FormLogin(request.POST)

    if form.is_valid():
      
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      
      mail_login = len(User.objects.filter(email=f"{email}"))
      password_login = len(User.objects.filter(senha=f"{password}"))
      
      if (mail_login > 0) and (password_login > 0):
        user = User.objects.filter(email=f"{email}")
        request.session["user"] = user[0].id

        return render(request, 'cidades/main.html')

      else:
        return render(request, 'cidades/login.html', { "form": FormLogin, 'isNot': True })        
              
    else:
      return render(request, 'cidades/login.html', { "form": FormLogin, 'isNotForm': True })
      
  else:
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