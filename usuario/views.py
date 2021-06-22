from django.shortcuts import render, redirect

def login(request):
  return render(request, 'usuario/login.html')

def cadastro(request):
  return render(request, 'usuario/cadastro.html')