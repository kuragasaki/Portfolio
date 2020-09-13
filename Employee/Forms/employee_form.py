#! Python3
# employee_form.py

from django import forms
from .login_form import LoginForm
from ..models.employee_model import EmployeeModel

class EmployeeForm(LoginForm):
    name = forms.CharField(label="名前", help_text='登録されている名前を入力')
    email = forms.CharField(label="メールアドレス", help_text='登録されているメールアドレスを入力')
    gender = forms.ChoiceField(label="性別", choices=[(0, "男性"), (1, "女性")], widget=forms.RadioSelect(), help_text='条件指定の場合はどちらか選択')
    date_of_joining = forms.DateField(label="入社年月日", help_text='条件指定の場合は')
    retirement_date = forms.DateField(label="退職年月日", required=False)
    admin_num = forms.BooleanField(label="管理者権限", required=False)
