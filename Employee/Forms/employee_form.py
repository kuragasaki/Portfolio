#! Python3
# login_form.py

from django import forms
from .login_form import LoginForm
from ..models.employee_model import EmployeeModel

class EmployeeForm(LoginForm):
    name = forms.CharField(label="名前", required=True, help_text='※必須')
#    email = forms.CharField(label="メールアドレス", required=True, help_text='※必須')
#    password = forms.CharField(label="パスワード", widget=forms.PasswordInput(), required=True, help_text='※必須')
#    password2 = forms.CharField(label="確認用パスワード", widget=forms.PasswordInput(), required=True, help_text='※必須')
    gender = forms.ChoiceField(label="性別", choices=[(0, "男性"), (1, "女性")], widget=forms.RadioSelect())
    date_of_joining = forms.DateField(label="入社年月日", required=True, help_text='※必須')
    retirement_date = forms.DateField(label="退職年月日", required=False)
    user_img = forms.ImageField(label="社員画像", required=False, help_text='※任意')
    admin_num = forms.BooleanField(label="管理者権限", required=False)

#    def __init__(self, params):
#        super(EmployeeForm, self)
#        super(EmployeeForm, self).__init__(params["mail"], params["password"])
#        self.name = ""
#        self.gender = 0

#    def save(self):
#        return "名前：{}, メアド：{}, パスワード：{}, 性別：{}, 社員画像：{}, 権限：{}".format(
#            self.cleaned_data.get("name")
#            , self.cleaned_data.get("mail")
#            , self.cleaned_data.get("password")
#            , self.cleaned_data.get("gender")
#            , self.cleaned_data.get("user_img")
#            , self.cleaned_data.get("admin_num"))
