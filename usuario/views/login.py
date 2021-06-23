from django.shortcuts import render, redirect

class Login:
  def to_login(request):
    return redirect('login/')

  def login(request):
    return render(request, 'usuario/login.html')