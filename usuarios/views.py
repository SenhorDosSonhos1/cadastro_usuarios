from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def cadastro(request):
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

def login(request):
    return HttpResponse('login')

def logout(request):
    return HttpResponse('logout')