#! Python3
# search_form.py

from django import forms

class SearchForm(forms.Form):
    name = forms.CharField(label="名前", required = False)
    email = forms.CharField(label="メールアドレス", required = False)
    gender = forms.ChoiceField(label="性別", required = False, choices=[(0, "男性"), (1, "女性")], widget=forms.RadioSelect(), help_text='条件指定の場合はどちらか選択')
    date_of_joining_before = forms.DateField(label="年月日", required = False, widget=forms.SelectDateWidget(years=[x for x in range(1990, 2100)]))
    date_of_joining_after = forms.DateField(label="年月日", required = False, widget=forms.SelectDateWidget(years=[x for x in range(1990, 2100)]))
    retirement_date_before = forms.DateField(label="年月日", required = False, widget=forms.SelectDateWidget(years=[x for x in range(1990, 2100)]))
    retirement_date_after = forms.DateField(label="年月日", required = False, widget=forms.SelectDateWidget(years=[x for x in range(1990, 2100)]))
    admin_num_choice = forms.ChoiceField(label="管理者権限", required = False, choices=[(0, "一般社員"), (1, "管理者")], widget=forms.RadioSelect(), help_text='条件指定の場合はどちらか選択')

