from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout




def index(request):
    return render(request, 'index.html')


@login_required
def logout(request):
    auth_logout(request) #nome da funcao alterado para nao ocorrer recursividade
    return redirect('index')