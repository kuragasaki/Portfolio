"""
from django.shortcuts import render
from django.http import HttpResponse

# 初期設定
params = {
    "title": "社員ログイン",
    "message": "",
    "login": "login",
    "form": login_form.LoginForm()
}


# 初期画面
def index(request):
    if request.method == 'POST':
        print("test")

    return render(request, 'employee/login.html', params)

def login(request):

    # ログインID（email）とパスワードが一致すれば、view画面へ遷移
    return render(request, 'employee/login.html', params)
"""