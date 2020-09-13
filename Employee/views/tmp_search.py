#! Python3
# edit_view.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from ..Forms.login_form import LoginForm
from ..Forms.employee_form import EmployeeForm
from ..models.login_model import LoginModel
from ..models.employee_model import EmployeeModel
from ..models.employee_model_form import EmployeeModelForm
from ..Logics import check_logic
from ..Logics import get_data_logic
from ..Logics import convert_logic

import os

class SearchView(TemplateView):
    def __init__(self):
        # 初期設定
        self.params = {
            "title": "登録内容確認",
            "retirement_date_flg": False,
            "next_page": "complete",
            "button_back": "修正",
            "button_complete_flg": True,
            "button_complete": "入力完了",
            "previous_page": "login",
            "previous_page_name": "ログイン画面へ",
            "emp_form": EmployeeModelForm(),
        }

    def get(self, request):

        # 不正アクセスされたいる。
        return render(request, 'employee/edit.html', self.params)

    def post(self, request):

        # 新規登録
        empForm = EmployeeModelForm(request.POST, request.FILES)
        self.params["emp_form"] = empForm

        # ログイン画面から遷移（ログインユーザーのIDが存在する）
        if "session_employee_id" in request.session:
            # 一覧画面から遷移するパターンを追加しよう
            # ログインユーザーがセッションに登録されているチェックと一覧画面からIDが取得の遷移ならOK

            empForm = EmployeeModelForm(EmployeeModel.objects.get(id = request.session["session_employee_id"]))
            self.params["button_complete_flg"] = False
            self.params["emp_form"] = empForm
            
        else:
            # 共通化しよう
            self.params["title"] = "社員登録"
            self.params["next_page"] = "complete"
            self.params["view_flg"] = True
            self.params["retirement_date_flg"] = False
            self.params["button_val"] = "入力完了"

            # formのバリデーションチェック
            if not empForm.is_valid():
                self.params["message"] = empForm.errors

            # メールアドレスがDBに存在しないかチェック
            elif check_logic.check_mailaddress(empForm["email"].data):
                self.params["message"] = "入力されたメールアドレスは、すでに登録されています。"

            # パスワードチェック
            elif empForm["password"].data != request.POST["password2"]:
                self.params["message"] = "入力されたパスワードと確認用パスワードの入力内容が一致しません。"

            # エラーが存在する
            if "message" in self.params and self.params["message"] != "":
                return render(request, 'employee/edit.html', self.params)
            
        # 新規登録、編集、確認、完了画面
        return render(request, 'employee/view.html', self.params)