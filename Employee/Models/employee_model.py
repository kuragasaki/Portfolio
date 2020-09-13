#! Python3
# employee_model.py
from django.db import models as django_models
from .login_model import LoginModel
#from datetime import datetime


class EmployeeModel(LoginModel):
    name = django_models.CharField(max_length = 20)
    gender = django_models.IntegerField(default = 0, choices=[(0, "男性"), (1, "女性")])
    date_of_joining = django_models.DateField(blank = False, null = False)
    retirement_date = django_models.DateField(blank = True, null = True)
    user_img = django_models.ImageField(upload_to='Employee/static/Employee/images',blank = True, null = True)
    admin_num = django_models.BooleanField(default = 0)
#    created_at = django_models.DateTimeField(auto_now=True, blank = False, null = False)
    #created_at = django_models.DateTimeField(editable = False, blank = False, null = False)
#    updated_at = django_models.DateTimeField(blank = True)

    def __str__(self):
        return "{} {} {} {} {} {} {} {}".format(
                self.name
                , self.email
                , self.password
                , self.gender
                , self.date_of_joining
                , self.retirement_date
                , self.user_img
                , self.admin_num
            )
