#! Python3
# search_view.py

from django.shortcuts import render
from django.views.generic import TemplateView
from ..Forms.search_form import SearchForm
from ..Forms.login_form import LoginForm
from ..Logics import get_data_logic
import datetime

class SearchView(TemplateView):
    def __init__(self):
        # 初期設定
        self.params = {
            "title": "社員検索",
            "message": "",
            "next_page": "search",
            "view_page": "preview",
            "method_type": "POST",
            "button_val": "検索",
            "emp_result_flg": False,
            "emp_result": [],
            "search_form": SearchForm()
        }

    def get(self, request):
        self.params["title"] = "社員ログイン"
        self.params["message"]: "アクセス方法に問題があります。"
        self.params["next_page"] = "login"
        self.params["button_val"] = "ログイン"
        self.params["form"] = LoginForm()
        return render(request, 'employee/login.html', self.params)

    def post(self, request):
#        import pdb #まずpdbをインポート
#        pdb.set_trace() #ここでset_trace()

        # 検索フォーム内容取得
        search_form = SearchForm(request.POST)

        # 条件設定
        where_dict = {}

        # email完全一致
        if bool(search_form["email"].data):
            where_dict["email"] = search_form["email"].data

        # name部分一致
        if bool(search_form["name"].data):
            where_dict["name__icontains"] = search_form["name"].data

        # gender完全一致
        if bool(search_form["gender"].data):
            where_dict["gender"] = search_form["gender"].data

        # date_of_joining 範囲、以上、以下
        if bool(search_form["date_of_joining_before"].data) or bool(search_form["date_of_joining_after"].data):
            message = set_date_where(where_dict, "date_of_joining", search_form["date_of_joining_before"].data, search_form["date_of_joining_after"].data)
            
            if bool(message):
                self.params["message"] = message
                return render(request, 'employee/search.html', self.params)

        # retirement_date 範囲、以上、以下
        if bool(search_form["retirement_date_before"].data) or bool(search_form["retirement_date_after"].data):
            message = set_date_where(where_dict, "retirement_date", search_form["retirement_date_before"].data, search_form["retirement_date_after"].data)

            if bool(message):
                self.params["message"] = message
                return render(request, 'employee/search.html', self.params)

        # admin_num完全一致
        if search_form["admin_num_choice"].data == 0:
            where_dict["admin_num_choice"] = False
        elif search_form["admin_num_choice"].data == 1:
            where_dict["admin_num_choice"] = True

        result = []
        if bool(where_dict):
            result = list(get_data_logic.get_employee_search(where_dict))
        else:
            result = list(get_data_logic.get_employees())

        if bool(result):
            self.params["emp_result"] = result
            self.params["emp_result_flg"] = True
        else:
            self.params["message"] = "検索条件に一致するデータは有りません。"            

        return render(request, 'employee/search.html', self.params)

def set_date_where(add_dict, column, before, after):
    column_name = "入社年月日"
    if column == "retirement_joining":
        column_name = "退職年月日"

    if bool(before) and bool(after):
        try:
            datetime.datetime.strptime(before, '%Y-%m-%d')
        except ValueError:
            return column_name + "の開始日付が正しくありません。"

        try:
            datetime.datetime.strptime(after, '%Y-%m-%d')
        except ValueError:
            return column_name + "の終了日付が正しくありません。"

        add_dict[ column + "__range"] = (before, after)

    else:
        if bool(before):
            try:
                datetime.datetime.strptime(before, '%Y-%m-%d')
            except ValueError:
                return column_name + "の開始日付が正しくありません。"

            add_dict[ column + "__gte"] = before

        elif bool(after):
            try:
                datetime.datetime.strptime(after, '%Y-%m-%d')
            except ValueError:
                return column_name + "の終了日付が正しくありません。"

            add_dict[column + "__lte"] = after

    return ""