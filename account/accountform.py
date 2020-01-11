from django import forms

class AccountForm(forms.Form):
    __account_id = forms.CharField(label='アカウントID', required=True)
    __password = forms.CharField(label='パスワード', required=True)
    __password2 = forms.CharField(label='確認用パスワード', required=True)
    __name = forms.CharField(label='名前')
#    __birthday = forms.DateField(label='生年月日')

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
    def password2(self):
        return self.__password2

    @password2.setter
    def password2(self, password2):
        self.__password2 = password2

    @property
    def name(self):
        return self.__password2

    @name.setter
    def name(self, name):
        self.__name = name

'''
    @property
    def birthday(self):
        return self.__password2

    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = birthday
'''