#! Python3
# login_form.py

from django import forms

class LoginForm(forms.Form):
    #email = forms.EmailField(label="メールアドレス", required=True, help_text='※必須')
    email = forms.CharField(label="メールアドレス", required=True, help_text='※必須')
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput(), required=True, help_text='※必須')

#    def __init__(self):
#        pass
"""
    def __init__(self, mail, password):
        self.mail = mail
        self.password = password
"""