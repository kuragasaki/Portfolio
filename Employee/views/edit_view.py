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
            "next_page": "edit",
            "method_type": "POST",
            "button_val": "確認",
            "action_type": "new",
            "user_img_flg": False,
            "admin_input_flg": True,
            "view_flg": True,
            "pw_edit_flg": False,
            "pw2_required": "required",
            "previous_page": "login",
            "previous_page_name": "ログイン画面へ",
#            "emp_form": EmployeeForm(),
            "emp_form": EmployeeModelForm(),
#            "login_form": LoginForm()
#            "form": EmployeeForm({"mail": "", "password": ""})
        }

    def get(self, request):

        # セッションに設定内容が存在する。
        if 'session_confirm' in request.session:
            empForm = EmployeeModelForm(request.session['session_confirm'], request.FILES)
#            empForm = EmployeeModelForm(request.session['session_confirm'], request.FILES, instance = EmployeeModel())
            self.params['emp_form'] = empForm
            del request.session['session_confirm']

        print("edit.view get")
        # 新規登録兼編集画面
        return render(request, 'employee/edit.html', self.params)


    def post(self, request):
        # 新規登録、更新、完了の分岐
        if request.POST["action_type"] in ["new", "update", "confirm"]:
            # 完了処理の場合はsessionから入力データ取得
            dir_name = ""
            if "confirm" in request.POST["action_type"]:
                empForm = EmployeeModelForm(request.session['session_confirm'], request.FILES)
#                empForm = EmployeeModelForm(request.session['session_confirm'], request.FILES, instance = EmployeeModel())
                del request.session['session_confirm']
                dir_name = empForm["email"].data.split("@")[0]

            elif "update" in request.POST["action_type"]:
                tmp_email = request.session['session_email']
                empForm = convert_logic.employeeModelToModelForm(EmployeeModel.objects.get(email = tmp_email))
                dir_name = empForm["email"].value().split("@")[0]
            else:
                #        empForm = EmployeeForm(request.POST)
                #empForm = EmployeeModelForm(request.POST, request.FILES, EmployeeModel())
                empForm = EmployeeModelForm(request.POST, request.FILES)
                dir_name = empForm["email"].data.split("@")[0]

            file_name = "画像無し"
            
            # 画像削除処理
            target_files = get_data_logic.get_upload_files(dir_name)
            
            # 画像のアップロード
            if 'user_img' in request.FILES:
                if bool(target_files):
                    for target_file in target_files:
                        os.remove(target_file)

                empForm.user_img = request.FILES['user_img']
                file_name = empForm.uploadFileToTempDir(dir_name)
                request.session["user_img"] = file_name
                self.params["user_img_flg"] = True

            elif "user_img" in request.session:
                file_name = request.session["user_img"]
                self.params["user_img_flg"] = True
                del request.session['user_img'] 

            # formのバリデーションチェック
            if empForm.is_valid():
                self.params["message"] = empForm.errors()

            self.params["emp_form"] = empForm

            # 新規登録の場合
            if request.POST["action_type"] == "new":
                # メールアドレスがDBに存在しないかチェック
                if check_logic.check_mailaddress(empForm["email"].data):
                    self.params["message"] = "入力されたメールアドレスは、すでに登録されています。"
                    self.params["user_img_flg"] = False
                    return render(request, 'employee/edit.html', self.params)

                # パスワードチェック
                if empForm["password"].data != request.POST["password2"]:
                    self.params["message"] = "入力されたパスワードと確認用パスワードの入力内容が一致しません。"
                    self.params["user_img_flg"] = False
                    return render(request, 'employee/edit.html', self.params)

                view_map = convert_logic.employeeFormToDict(["name", "email", "date_of_joining", "retirement_date"], empForm)
                view_map["password"] = "セキュリティの観点から入力された値は表示されません。"
                view_map["gender"] = "男性" if empForm["gender"].data == "0" else "女性"
                view_map["user_img"] = file_name
                view_map["admin_num"] = "管理職" if empForm["admin_num"].data else "社員"
                self.params["emp_form"] = view_map

            if request.POST["action_type"] != "update":
                # 新規登録・確認共通設定
                self.params["admin_input_flg"] = True
                self.params["view_flg"] = False
                self.params["pw2_required"] = ""
            else:
                self.params["user_img_flg"] = False


            # 確認後、保存処理
            if request.POST["action_type"] == "confirm":
#                empForm.insert()

                emp_model = EmployeeModel(
                    name = empForm["name"].data
                    , email = empForm["email"].data
                    , password = empForm["password"].data
                    , gender = empForm["gender"].data
                    , date_of_joining = empForm["date_of_joining"].data
                    , retirement_date = empForm["retirement_date"].data
                    , user_img = file_name
                    , admin_num = empForm["admin_num"].data
                )
                emp_model.save()


                print("150行目")
#                import pdb; 58.92 / 6 + 130.535
#                pdb.set_trace()
#                print(type(empForm))
#                empForm.save()
                self.params["next_page"] = "login"
                self.params["method_type"] = "POST"
                self.params["button_val"] = "ログイン"
                self.params["action_type"] = None
                self.params["message"] = "以下の内容で登録が完了しました。"

            # 新規登録、更新の際の設定内容
            else:
                self.params["previous_page"] = "edit"
                self.params["action_type"] = "confirm"
                self.params["message"] = "以下の内容で登録しますが、よろしいですか？"
                self.params["previous_page_name"] = "内容の修正"
                self.params["button_val"] = "登録"

                request.session['session_confirm'] = request.POST


        # 確認後、保存処理
        if request.POST["action_type"] == "confirm":
            print("{} {}".format(
                    self.params["next_page"]
                    , self.params["method_type"]
                )
            )

        # 新規登録、編集、確認、完了画面
        return render(request, 'employee/edit.html', self.params)