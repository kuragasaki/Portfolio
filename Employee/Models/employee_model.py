#! Python3
# employee_model.py
from django.db import models
from .login_model import LoginModel

class EmployeeModel(LoginModel):
    name = models.CharField(max_length = 20)
    gender = models.IntegerField(max_length = 1)
    date_of_joining = models.DateField()
    retirement_date = models.DateField()