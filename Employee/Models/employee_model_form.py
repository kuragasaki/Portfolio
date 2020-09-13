#! Python3
# employee_model_form.py
from django import forms
from django.shortcuts import redirect
from django.conf import settings
#from django.core.urlresolvers import reverse
from django.conf.urls.static import static
from django.core.files.storage import default_storage
#from django.contrib.admin.widgets import AdminDateWidget
#from django.contrib.formtools.preview import FormPreview
from ..models.employee_model import EmployeeModel 
from ..Logics import check_logic
import os

class EmployeeModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required = True)
    gender = forms.ChoiceField(label="性別", choices=[(0, "男性"), (1, "女性")], widget=forms.RadioSelect())

    date_of_joining = forms.DateField(label="入社年月日", required=True, widget=forms.SelectDateWidget(years=[x for x in range(1990, 2100)]))
    retirement_date = forms.DateField(label="退職年月日", required=False, widget=forms.SelectDateWidget(years=[x for x in range(1990, 2100)]))
    #date_of_joining = forms.DateField(label="入社年月日", required=True, widget=AdminDateWidget())
    #retirement_date = forms.DateField(label="退職年月日", required=False, widget=AdminDateWidget())
    
    user_img = forms.ImageField(label="社員画像", required=False)
    admin_num = forms.BooleanField(label="管理者権限", required=False)
    class Meta:
        model = EmployeeModel
        fields = ["name", "email", "password", "gender", "date_of_joining", "retirement_date", "user_img", "admin_num"]
        widgets = {
            'user_img': forms.ClearableFileInput(attrs={
            }),
        }

    def uploadFileToTempDir(self, dir_name):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        app_name = base_dir.split(os.sep)[-1]
        file_name = dir_name + self.user_img.name[self.user_img.name.rindex("."):]
        image_root = os.sep.join([base_dir + settings.STATIC_URL + app_name, "images", dir_name, file_name])
        default_storage.save(image_root, self.user_img)
        if not check_logic.check_face_image(image_root, file_name):
            # チェックエラーで削除処理
            return False

        return dir_name + os.sep + file_name

    """
    def save(self):
        print(self.__str__())
        print(type(self.Meta.model))
        print(self.Meta.model)
        print("save関数実行")
        model = EmployeeModel()
        model.name = self.Meta.model.name
        model.email = self.Meta.model.email
        model.password = self.Meta.model.password
        model.gender = self.Meta.model.gender
        model.date_of_joining = self.Meta.model.date_of_joining
        model.retirement_date = self.Meta.model.retirement_date
        model.user_img = self.Meta.model.user_img
        model.admin_num = self.Meta.model.admin_num
        print("save前")
        print(model)
        model.save()
        print("保存完了")
    """
    """
    def insert(self):
        empModel = EmployeeModel(
            name = self.Meta.model.name
            , email = self.Meta.model.email
            , password = self.Meta.model.password
            , gender = self.Meta.model.gender
            , date_of_joining = self.Meta.model.date_of_joining
            , retirement_date = self.Meta.model.retirement_date
            , user_img = self.Meta.model.user_img
            , admin_num = self.Meta.model.admin_num
        )

        empModel.save()
    """

    def __str__(self):
        return "{} {} {} {} {} {} {} {}".format(
                self.Meta.model.name
                , self.Meta.model.email
                , self.Meta.model.password
                , self.Meta.model.gender
                , self.Meta.model.date_of_joining
                , self.Meta.model.retirement_date
                , self.Meta.model.user_img
                , self.Meta.model.admin_num
            )

"""
class EmployeeModelFormPreview(FormPreview):

    def done(self, request, cleaned_data):
        empModel = EmployeeModel(**cleaned_data)
        empModel.save()
        return redirect(reverse('emplyee_created', args=(), kwargs={}))
"""