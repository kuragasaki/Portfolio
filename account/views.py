from django.shortcuts import render
from django.http import HttpResponse
from .accountform import AccountForm
# Create your views here.

def index(request):
    return HttpResponse("Hello Portfolio")

def login(request):
    params = {
        'title': 'Login画面',
        'goto': 'edit',
    }
    return render(request, "account/login.html", params)

def edit(request):

    title = '登録画面'
    params = {
        'title': title,
        'goto': 'login',
        'next': 'edit',
        'form':  AccountForm(),
    }

    if request.method == 'POST':
        title = '確認画面'
        params = {
        'title': title,
        'goto': 'login',
        'next': 'edit',
        'form':  AccountForm(),
        }
        return render(request, "account/edit.html", params)

    return render(request, "account/edit.html", params)