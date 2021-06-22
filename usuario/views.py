from django.shortcuts import render, redirect

def to_login(request):
  return redirect('login/')

def login(request):
  return render(request, 'usuario/login.html')

def cadastro(request):
  return render(request, 'usuario/cadastro.html')

def esqueceu_senha(request):
  return render(request, 'usuario/esqueceu-senha.html')