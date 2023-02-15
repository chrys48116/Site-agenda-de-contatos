from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    
    user = request.POST.get('user')
    password = request.POST.get('password')

    user_authentic = auth.authenticate(request, username=user, password=password)

    if not user or not password:
        messages.error(request, 'Usuario ou senha invalidos')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user_authentic)
        messages.success(request, 'Logado com sucesso!')
        return redirect('dashboard')
        

def logout(request):
    auth.logout(request)
    return redirect('dashboard')

def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')
    
    name = request.POST.get('name')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    user = request.POST.get('user')
    password = request.POST.get('password')
    reap_password = request.POST.get('reap_password')

    if not name or not sobrenome or not email or not user or not password or not reap_password:
        messages.error(request, 'Alguns campos em branco devem ser preenchidos!')
        return render(request, 'accounts/register.html')
    
    try:
        validate_email(email)
    except:
        messages.error(request, 'Email invalido.')
        return render(request, 'accounts/register.html')
    
    if len(user) < 6:
        messages.error(request, 'O nome de usuario deve possuir pelo menos 6 caracteres.')
        return render(request, 'accounts/register.html')

    if len(password) and len(reap_password) < 6:
        messages.error(request, 'A senha deve possuir pelo menos 6 caracteres.')
        return render(request, 'accounts/register.html')
    
    elif password != reap_password:
        messages.error(request, 'As senhas devem ser iguais.')
        return render(request, 'accounts/register.html')
    
    if User.objects.filter(username=user).exists():
        messages.error(request, 'Usuario já existente')
        return render(request, 'accounts/register.html')
    
    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já cadastrado')
        return render(request, 'accounts/register.html')

    messages.success(request, 'Usuario cadastrado com sucesso! Faça login')
    
    user_register = User.objects.create_user(username=user, email=email, 
                                           password=password, 
                                           first_name=name, 
                                           last_name=sobrenome)
    user_register.save()
    return redirect('login')

@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
