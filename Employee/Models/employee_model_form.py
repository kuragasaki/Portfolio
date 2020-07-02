#! Python3
# employee_model.py
from django import forms
from django.conf import settings
from django.conf.urls.static import static
from django.core.files.storage import default_storage
from ..models.employee_model import EmployeeModel 
import os

class EmployeeModelForm(forms.ModelForm):
#    name = forms.CharField(label="名前", required = True)
#    email = forms.EmailField(label = "メールアドレス", required = True)
    password = forms.CharField(widget=forms.PasswordInput, required = True)
    gender = forms.ChoiceField(label="性別", choices=[(0, "男性"), (1, "女性")], widget=forms.RadioSelect())

    date_of_joining = forms.DateField(label="入社年月日", required=True)
    retirement_date = forms.DateField(label="退職年月日", required=False)
    user_img = forms.ImageField(label="社員画像", required=False)
    admin_num = forms.BooleanField(label="管理者権限", required=False)
    class Meta:
        model = EmployeeModel
        fields = ["name", "email", "password", "gender", "date_of_joining", "retirement_date", "user_img", "admin_num"]
        widgets = {
            'user_img': forms.ClearableFileInput(attrs={

            })
        }

    def uploadFileToTempDir(self, dir_name):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        app_name = base_dir.split(os.sep)[-1]
        file_name = dir_name + self.user_img.name[self.user_img.name.rindex("."):]
        image_root = os.sep.join([base_dir + settings.STATIC_URL + app_name, "images", file_name])
        default_storage.save(image_root, self.user_img)
        return file_name

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