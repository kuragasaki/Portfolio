from django import forms

class LoginForm(forms.Form):
    _account_id = forms.CharField(label='アカウントID')
    _password = forms.CharField(label='パスワード')

    def __init__(self, accound_id, password):
        self._account_id = accound_id
        self._password = password

