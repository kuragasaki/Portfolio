#! Python3
# form_preview.py

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

class FormPreview(TemplateView):
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
        self.params["title"] = "社員ログイン"
        self.params["message"]: "アクセス方法に問題があります。"
        self.params["next_page"] = "login"
        self.params["button_val"] = "ログイン"
        self.params["form"] = LoginForm()
        return render(request, 'employee/login.html', self.params)

    def post(self, request):
#        import pdb; pdb.set_trace()
        # 新規登録
        empForm = EmployeeModelForm(request.POST, request.FILES)

        # 選択されたIDに紐づくEmployeeレコードを取得。
        if "search_id" in request.POST:
            search_emp = get_data_logic.get_employee_search({"id": request.POST["search_id"]})[0]
            request.session["session_employee_email"] = search_emp.email
            empForm = EmployeeModelForm(instance = search_emp)

        self.params["gender_flg"] = False
        
        if empForm["gender"].value() == str(0):
            self.params["gender_flg"] = True
        
        self.params["emp_form"] = empForm

        # ログイン画面から遷移（ログインユーザーのIDが存在する）
        if "session_employee_email" in request.session:
            # 一覧画面から遷移するパターンを追加しよう
            # ログインユーザーがセッションに登録されているチェックと一覧画面からIDが取得の遷移ならOK

            errors = ""
            # formのバリデーションチェック
            if not empForm.is_valid():

                if "name" in empForm.errors:
                    errors += "名前の入力内容が正しくありません。<br />"

                if "gender" in empForm.errors:
                    errors += "性別が正しく選択されていません。<br />"

            # エラーが存在する
            if errors != "":
                self.params["view_flg"] = True
                self.params["pw2_required"] = ""
                self.params["title"] = "登録内容修正"
                self.params["next_page"] = "preview"
                self.params["button_val"] = "修正完了"
                self.params["message"] = errors

                return render(request, 'employee/edit.html', self.params)

            if bool(empForm["retirement_date"].data):
                self.params["retirement_date_flg"] = True

            # ファイルを一時保存
            """　後々後から画像を修正する処理を追加
            if "user_img" in request.FILES:
                empForm.user_img = request.FILES['user_img']
                self.params["img_name"] = empForm.uploadFileToTempDir(empForm["email"].data.split("@")[0])
                request.session["img_name"] = self.params["img_name"]
            """
            img_dict = EmployeeModel.objects.values("user_img").get(email = request.session["session_employee_email"])
            self.params["img_name"] = ""
            if bool(img_dict["user_img"]):
                self.params["img_name"] = img_dict["user_img"]
                request.session["img_name"] = self.params["img_name"]

            self.params["button_complete_flg"] = False
            if "edit_button" in request.POST:
                self.params["button_complete_flg"] = True

        else:

            errors = ""
            # formのバリデーションチェック
            if not empForm.is_valid():

                if "name" in empForm.errors:
                    errors += "名前の入力内容が正しくありません。<br />"

                if "email" in empForm.errors:
                    errors += "メールアドレスが正しくありません。<br />"        

                if "password" in empForm.errors:
                    errors += "パスワードの入力内容が正しくありません。<br />"

                if "date_of_joining" in empForm.errors:
                    errors += "入社年月日の入力内容が正しくありません。<br />"

                if "gender" in empForm.errors:
                    errors += "性別が正しく選択されていません。<br />"

            # メールアドレスがDBに存在しないかチェック
            if check_logic.check_mailaddress(empForm["email"].data):
                errors += "入力されたメールアドレスは、すでに登録されています。<br />"

            # パスワードチェック
            if empForm["password"].data != request.POST["password2"]:
                errors += "入力されたパスワードと確認用パスワードの入力内容が一致しません。<br />"

            self.params["img_name"] = ""
            # ファイルを一時保存
            if "user_img" in request.FILES:
                empForm.user_img = request.FILES['user_img']
                # 顔認証処理兼アップロード
                fileUploadResult = empForm.uploadFileToTempDir(empForm["email"].data.split("@")[0])
                if fileUploadResult:
                    self.params["img_name"] = fileUploadResult
                    request.session["img_name"] = self.params["img_name"]

                else:
                    errors += "アップロードされた画像で顔が認識出来ませんでした。"
            else:
                if "img_name" in request.session:
                    del request.session["img_name"]

            # エラーが存在する
            if errors != "":
                self.params["view_flg"] = True
                self.params["title"] = "社員登録"
                self.params["pw2_required"] = "required"
                self.params["next_page"] = "preview"
                self.params["button_val"] = "入力完了"
                self.params["message"] = errors

                return render(request, 'employee/edit.html', self.params)

            # 正常パターン
            self.params["title"] = "登録内容確認"
            self.params["next_page"] = "complete"
            self.params["retirement_date_flg"] = False

        # 新規登録、編集、確認、完了画面
        return render(request, 'employee/view.html', self.params)