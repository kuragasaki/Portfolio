#! Python3
# login_view.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from ..Forms.login_form import LoginForm
from ..Forms.search_form import SearchForm
from ..Forms.employee_form import EmployeeForm
from ..models.employee_model_form import EmployeeModelForm
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
#        import pdb #まずpdbをインポート
#        pdb.set_trace() #ここでset_trace()

        # logic処理を挟もう
        if check_logic.check_login(LoginForm(request.POST)):
            self.params["message"] = "メールアドレス、または、パスワードが間違えています。"
            return render(request, 'employee/login.html', self.params)
        
        email = request.POST["email"]
        emp_form = get_data_logic.get_employee_search({"email": email})[0]

        self.params["gender_flg"] = False
        if emp_form.gender == 0:
             self.params["gender_flg"] = True

        # ファイルを一時保存
        if bool(emp_form.user_img):
            self.params["img_name"] = str(emp_form.user_img)
            request.session["img_name"] = self.params["img_name"]

        else:
            self.params["img_name"] = ""

        self.params["emp_form"] = EmployeeModelForm(instance = emp_form)

        # 管理者権限持ちかチェック（持っていれば、一覧（検索）画面へ
        if emp_form.admin_num:
            employees = get_data_logic.get_employees()

            # パラメーター変更、追加
            self.params["title"] = "社員検索"
            self.params["next_page"] = "search"
            self.params["method_type"] = "POST"
            self.params["button_val"] = "検索"
            self.params["emp_result_flg"] = False
            self.params["employees"] = employees
            self.params["search_form"] = SearchForm()

            request.session['session_login'] = request.POST

            # 遷移先変更
            return render(request, 'employee/search.html', self.params)

        self.params["title"] = "詳細表示"
        self.params["next_page"] = "complete"
        self.params["method_type"] = "POST"
        self.params["button_back"] = "修正"
        self.params["button_complete_flg"] = False
        self.params["previous_page"] = "login"
        self.params["previous_page_name"] = "ログイン画面へ"
        request.session["session_employee_email"] = email

        # 社員情報表示画面へ
        return render(request, 'employee/view.html', self.params)

