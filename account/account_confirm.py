from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .accountform import AccountForm
# Create your views here.

class AccountConfirm(TemplateView):

    def __init__(self):
        self.params = {
            'title': '確認画面',
            'goto': 'login',
            'next': 'confirm',
            'button_view': 'ログイン画面へ',
            'message': '登録完了',
            'form':  AccountForm(),
        }

    def post(self, request):
      #  accountForm = request.session['session_confirm']
        self.params["form"] = AccountForm(request.session['session_confirm'])

        ## DB登録実施
        ## 登録成功有無
        self.params["title"] = '登録完了画面'
        self.params['next'] = "login"

        # self.params["message"] = '登録失敗しました。再度入力してください。'
        return render(request, "account/account_confirm.html", self.params)
