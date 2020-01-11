from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .accountform import AccountForm
# Create your views here.

class AccountEdit(TemplateView):

    def __init__(self):
        self.params = {
            'title': '登録画面',
            'goto': 'login',
            'next': 'edit',
            'button_view': '登録',
            'form':  AccountForm(),
        }

    def get(self, request):
        return render(request, "account/account_edit.html", self.params)

    def post(self, request):
        self.params["title"] = '確認画面'
        self.params['form'] = AccountForm(request.POST)
        self.params["next"] = 'confirm'

        return render(request, "account/account_confirm.html", self.params)