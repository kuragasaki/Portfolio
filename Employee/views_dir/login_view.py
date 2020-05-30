#! Python3
# login_view.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from ..Forms import login_form


class LoginView(TemplateView):
    def __init__(self):
        # 初期設定
        self.params = {
            "title": "社員ログイン",
            "message": "",
            "login": "login",
            "form": login_form.LoginForm()
        }

    def get(self, request):
        # TODO パラメータ付きURLはIDとメールアドレスだけを表示させるパターンも実装する。
        return render(request, 'employee/login.html', self.params)

    def post(self, request):
        # TODO メールアドレス、パスワードチェック
        if not request.POST["mail"]:
            print("メール未入力")

        if not request.POST["password"]:
            print("パスワード未入力")

        """
        self.params["title"] = '確認画面'
        self.params["next"] = 'confirm'
        self.params["goto"] = 'edit'
        """
#        request.session['session_confirm'] = accountForm
#        request.session['session_confirm'] = request.POST

        # TODO 管理者権限持ちかチェック（持っていれば、一覧（検索）画面へ
        return render(request, 'employee/login.html', self.params)




