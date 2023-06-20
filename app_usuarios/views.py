from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout


def cadastro(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "GET":
        return render(request, 'cadastro.html')

    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not all([nome, email, senha, confirmar_senha]):
            messages.error(request, 'Preencha todos os campos')
            return render(request, 'cadastro.html')

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não correspondem')
            return render(request, 'cadastro.html')

        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            messages.success(request, 'Cadastro realizado com sucesso')
            return redirect('login')

        except Exception as e:
            messages.error(request, 'Erro ao realizar o cadastro')
            return render(request, 'cadastro.html')


def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not nome or not senha:
            messages.error(request, 'Preencha todos os campos')
            return render(request, 'login.html')

        if User.objects.filter(username=nome).exists():
            user = authenticate(username=nome, password=senha)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Usuário ou senha inválidos')
        else:
            messages.error(request, 'Usuário não existe')

        return render(request, 'login.html')


def sair(request):
    logout(request)
    return redirect('/')


def home(request):
    return render(request, 'home.html')


def cadastrar(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "GET":
        return render(request, 'cadastro.html')

    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not all([nome, email, senha, confirmar_senha]):
            messages.error(request, 'Preencha todos os campos')
            return render(request, 'cadastro.html')

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não correspondem')
            return render(request, 'cadastro.html')

        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            messages.success(request, 'Cadastro realizado com sucesso')
            return redirect('login')

        except Exception as e:
            messages.error(request, 'Erro ao realizar o cadastro')
            return render(request, 'cadastro.html')


