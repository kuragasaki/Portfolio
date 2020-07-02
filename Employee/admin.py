from django.contrib import admin

# Register your models here.
from .models.login_model import LoginModel
from .models.employee_model import EmployeeModel

admin.site.register(LoginModel)
admin.site.register(EmployeeModel)