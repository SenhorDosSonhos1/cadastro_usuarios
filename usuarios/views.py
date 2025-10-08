from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def usuario_cadastro(request):
    if request.method == "POST":
        nome_usuario = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("password")
        #Adicionar validação
        confirmar_senha = request.POST.get("confirm_password")
        
        if senha != confirmar_senha:
            messages.error(request, "As senhas não coincidem")
            return redirect(reverse('cadastro'))
        
        if User.objects.filter(username = nome_usuario, email = email).exists():
            messages.warning(request, "Nome de usuário já está em uso.")
        
        user = User.objects.create_user(
            username = nome_usuario,
            email = email,
            password = senha
        )
        messages.success(request, "Conta criada com sucesso! Faça login.")
        return redirect(reverse('login'))
    
    return render(request, 'cadastro.html')

def usuario_login(request):
    if request.method == "POST":
        nome_usuario = request.POST.get("username")
        senha = request.POST.get("password")

        usuario = authenticate(username = nome_usuario, password = senha)

        if usuario is not None:
            login(request, usuario)
            messages.success(request, f"Bem-vindo(a), {nome_usuario}!")
            return redirect(reverse('home'))
        
        messages.error(request,'Não existe um usuario com essas credenciais')
        return redirect(reverse('login'))

            
    return render(request, 'login.html')

def usuario_logout(request):
    logout(request)
    messages.info(request, "Você saiu da sua conta.")
    return redirect(reverse('login'))