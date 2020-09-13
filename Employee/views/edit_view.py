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

class EditView(TemplateView):
    def __init__(self):
        # 初期設定
        self.params = {
            "title": "社員登録",
            "message": "",
            "next_page": "preview",
            "view_flg": True,
            "pw2_required": "required",
            "button_val": "入力完了",
            "previous_page": "login",
            "previous_page_name": "ログイン画面へ",
            "emp_form": EmployeeModelForm(),
        }

    def get(self, request):
        if "session_employee_email" in request.session:
            del request.session["session_employee_email"]

        if "img_name" in request.session:
            del request.session["img_name"]

        # 新規登録兼編集画面
        return render(request, 'employee/edit.html', self.params)

    def post(self, request):
#        import pdb; pdb.set_trace()

        # 新規登録
        empForm = EmployeeModelForm(request.POST, request.FILES)
        self.params["emp_form"] = empForm
        # ログイン画面から遷移（ログインユーザーのIDが存在する）
#        if "session_employee_id" in request.session:
            # 一覧画面から遷移するパターンを追加しよう
            # ログインユーザーがセッションに登録されているチェックと一覧画面からIDが取得の遷移ならOK

#            empForm = EmployeeModelForm(EmployeeModel.objects.get(id = request.session["session_employee_id"]))
#            self.params["view_flg"] = False
#            self.params["pw2_required"] = ""
#            self.params["button_val"] = "修正"

#        elif "session_confirm" in request.session:
#            empForm = EmployeeModelForm(request.session["session_confirm"])

#        self.params["emp_form"] = empForm

        
        # 新規登録、編集、確認、完了画面
        return render(request, 'employee/edit.html', self.params)

