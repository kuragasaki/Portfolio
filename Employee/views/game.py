#! Python3
# edit_view.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from ..Forms.login_form import LoginForm

class GameView(TemplateView):
    def get(self, request, **args):
        if "test_id" in request.GET:
            test_id = request.GET["test_id"]

            if test_id == 0:
                # 初期設定
                self.params = {
                    "title": "社員ログイン",
                    "message": "",
                    "next_page": "login",
                    "button_val": "ログイン",
                    "form": LoginForm()
                }

            return render(request, 'employee/login.html', self.params)

        # ゲーム画面
        return render(request, 'employee/game.html', {})
        #return render(request, 'employee/login.html', self.params)

    def post(self, request):

        return render(request, 'employee/login.html', {})
