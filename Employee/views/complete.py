#! Python3
# complete.py
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from ..Forms.login_form import LoginForm
from ..Forms.employee_form import EmployeeForm
from ..models.employee_model_form import EmployeeModelForm
from ..models.employee_model import EmployeeModel
from ..Logics import check_logic
from ..Logics import convert_logic
from ..Logics import get_data_logic
import os
import shutil

class CompleteView(TemplateView):
    def __init__(self):
        # 初期設定
        self.params = {
            "title": "登録完了",
            "message": "登録が完了しました。",
            "next_page": "login",
            "button_val": "ログイン",
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

        # 押されたボタンによって修正画面へ遷移させるかどうかを判定する。
        if "next_action" not in request.POST:
            # 不正な画面遷移
            return render(request, 'employee/login.html', self.params)

        # パラメータ設定が必要
        empForm = EmployeeModelForm(request.POST, request.FILES)

        if "back" in request.POST["next_action"]:
            # ディレクトリから画像ファイル削除
            view_flg = True
            page_title = "社員登録"
            button_val = "入力完了"
            required_flg = "required"
            self.params["message"] = ""

            if "session_employee_email" in request.session:
                view_flg = False
                page_title = "登録内容修正"
                button_val = "修正完了"
                required_flg = ""

                # 性別の画面表示用
                self.params["gender_flg"] = str(empForm["gender"].data) == "0"

                # 画像情報取得
                ## 列指定しないといけない
                img_dict = EmployeeModel.objects.values("user_img").get(email = empForm["email"].data)
                self.params["img_name"] = ""
                if bool(img_dict["user_img"]):
                    self.params["img_name"] = img_dict["user_img"]

            # アップロードファイル確認
            elif "img_name" in request.session:
                # ディレクトリ
                file_name = empForm["email"].data.split("@")[0]
#                base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                app_name = settings.BASE_DIR.split(os.sep)[-1]
                image_root = os.sep.join([settings.BASE_DIR + settings.STATIC_URL + app_name, "images", file_name])

                # 画像削除
                if os.path.isdir(image_root):
                    shutil.rmtree(image_root)

            # 共通化しよう
            self.params["title"] = page_title
            self.params["next_page"] = "preview"
            self.params["view_flg"] = view_flg
            self.params["pw2_required"] = required_flg
            self.params["button_val"] = button_val
            self.params["previous_page"] = "login"
            self.params["previous_page_name"] = "ログイン画面へ"
            self.params["emp_form"] = empForm
 
            # 登録完了を表示
            return render(request, 'employee/edit.html', self.params)

        # すでに登録済のユーザーだった場合は、タイトルとメッセージを修正する。
        if "session_employee_email" in request.session:
            search_emp = get_data_logic.get_employee_search({"email": request.session["session_employee_email"]})[0]
            emp_update = EmployeeModelForm(request.POST, instance = search_emp)
            emp_update.save()
            self.params["title"] = "修正完了"
            self.params["message"] = "修正が完了しました。"
            del request.session["session_employee_email"]

            if "img_name" in request.session:
                del request.session["img_name"]
        else:
            # DB保存処理
            empForm.save()

            # 画像設定
            if "img_name" in request.session:
                empModel = EmployeeModel.objects.get(email = empForm["email"].data)
                empModel.user_img =  request.session["img_name"]
                empModel.save()
                del request.session["img_name"]

        # 登録完了を表示
        return render(request, 'employee/complete.html', self.params)