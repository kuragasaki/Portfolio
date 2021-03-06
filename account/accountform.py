from django import forms

class AccountForm(forms.Form):
    account_id = forms.CharField(label='アカウントID', required=True)
#    account_id = forms.EmailField(label='アカウントID', required=True)
    name = forms.CharField(label='名前')
#    __birthday = forms.DateField(label='生年月日')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput(), required=True)
#    password2 = forms.CharField(label='確認用パスワード', required=True)

'''

    @property
    def account_id(self):
        return self.__account_id

    @account_id.setter
    def account_id(self, account_id):
        self.__account_id = account_id

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def name(self):
        return self.__password2

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def password2(self):
        return self.__password2

    @password2.setter
    def password2(self, password2):
        self.__password2 = password2


    @property
    def birthday(self):
        return self.__password2

    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = birthday
'''