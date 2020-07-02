#! Python3
# login_view.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from ..Forms.login_form import LoginForm
from ..Forms.employee_form import EmployeeForm
from ..Logics import check_logic
from ..Logics import convert_logic
from ..Logics import get_data_logic

class LoginView(TemplateView):
    def __init__(self):
        # 初期設定
        self.params = {
            "title": "社員ログイン",
            "message": "",
            "next_page": "login",
            "button_val": "ログイン",
            "form": LoginForm()
        }

    def get(self, request):
        # TODO パラメータ付きURLはIDとメールアドレスだけを表示させるパターンも実装する。
        return render(request, 'employee/login.html', self.params)

    def post(self, request):

        print("login.view post")
        # logic処理を挟もう
        if check_logic.check_login(LoginForm(request.POST)):
            self.params["message"] = "メールアドレス、または、パスワードが間違えています。"
            return render(request, 'employee/login.html', self.params)
        
        email = request.POST["email"]
        employee_info = get_data_logic.get_employee_search({"email": email})
        print("get_employee_search(type_dict)")
        print(employee_info)
        print(type(employee_info))
        emp_form = convert_logic.employeeModelToDict(employee_info)[0]
        self.params["emp_form"] = emp_form

        # 管理者権限持ちかチェック（持っていれば、一覧（検索）画面へ
        if emp_form["admin_num"] == "管理職":
            employees = get_data_logic.get_employees()

            # パラメーター変更、追加
            self.params["title"] = "社員一覧"
            self.params["next_page"] = "search"
            self.params["button_val"] = "検索"
            self.params["employees"] = employees

            request.session['session_login'] = request.POST

            # 遷移先変更
            return render(request, "", self.params)

        self.params["title"] = "詳細表示"
        self.params["next_page"] = "edit"
        self.params["button_val"] = "修正"
        self.params["method_type"] = "POST"
        self.params["action_type"] = "update"

        if emp_form["user_img"] != "画像無し":
            self.params["user_img_flg"] = True
        else:
            self.params["user_img_flg"] = False
            
        self.params["view_flg"] = False
        self.params["pw_edit_flg"] = False
        self.params["pw2_required"] = "required"
        self.params["previous_page"] = "login"
        self.params["previous_page_name"] = "ログイン画面へ"
        request.session["session_email"] = email
        request.session['session_login'] = request.POST

        # 社員情報表示画面へ
        return render(request, 'employee/edit.html', self.params)

