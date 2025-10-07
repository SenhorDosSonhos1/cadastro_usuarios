from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def usuario_cadastro(request):
    if request.method == "POST":
        nome_usuario = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("password")
        confirmar_senha = request.POST.get("confirm_password")
        
        if User.objects.filter(email = email).exists():
            return HttpResponse("Usuario ja existe")
        
        user = User.objects.create_user(
            username = nome_usuario,
            email = email,
            password = senha
        )

        return redirect(reverse('login'))
    return render(request, 'cadastro.html')

def usuario_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("password")

        usuario = authenticate(email = email, password = senha)

        if usuario is not None:
            login(request, usuario)
            return HttpResponse("Logado")
            login(request, usuario)
        return HttpResponse("Não existe um usuario com essas credenciais")
            
    return render(request, 'login.html')

def usuario_logout(request):
    logout(request)
    return redirect(reverse('login'))