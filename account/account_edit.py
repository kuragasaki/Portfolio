import json
from Crypto.Cipher import AES
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.serializers.json import DjangoJSONEncoder
from .accountform import AccountForm
from .tmp_file_CRUD import account_file
# Create your views here.

class AccountEdit(TemplateView):

    def __init__(self):
        self.params = {
            'title': '登録画面',
            'goto': 'login',
            'next': 'edit',
            'button_view': '登録',
            'message': '',
            'form':  AccountForm(),
        }

    def get(self, request):
        # セッションを持ったままであれば、削除する
        if 'session_confirm' in request.session:
            self.params['form'] = AccountForm(request.session['session_confirm'])
            del request.session['session_confirm']
        return render(request, "account/account_edit.html", self.params)

    def post(self, request):
        #accountForm = AccountForm(request.POST) 
        accountForm = AccountForm(request.POST)

#        account_file(request.POST, True)
        account_file(accountForm, True)
        self.params['form'] = accountForm
        if not request.POST["password"] == request.POST["password2"]:
            return render(request, "account/account_edit.html", self.params)

        self.params["password2"] = request.POST["password2"]
        self.params["title"] = '確認画面'
        self.params["next"] = 'confirm'
        self.params["goto"] = 'edit'

#        request.session['session_confirm'] = accountForm
        request.session['session_confirm'] = request.POST

        return render(request, "account/account_confirm.html", self.params)
