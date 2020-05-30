#! Python3
# login_form.py

from django import forms

class LoginForm(forms.Form):
    mail = forms.CharField(label="メールアドレス", required=True)
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput(), required=True)
