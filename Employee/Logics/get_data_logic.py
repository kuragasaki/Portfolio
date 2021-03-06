#! Python3
# get_data_logic.py
from django.conf import settings
from ..Forms.login_form import LoginForm
from ..Forms.employee_form import EmployeeForm
from ..models.login_model import LoginModel
from ..models.employee_model import EmployeeModel
from ..models.employee_model_form import EmployeeModelForm

from PIL import Image

import glob
import os

def get_employees():
    return EmployeeModelForm.Meta.model.objects.all()

## 列名と値を辞書型にして、受け取り、検索する。
## 例 {"email": "test@gmail.com"}
def get_employee_search(type_dict):
    # DBからメールアドレスを条件にレコードを取得
    emp_model = EmployeeModelForm.Meta.model.objects.filter(**type_dict)
    return emp_model

def get_employee_like_name():
    pass

# アップロード済のファイルを取得する
def get_upload_files(file_name):
#    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#    app_name = base_dir.split(os.sep)[-1]
    app_name = settings.BASE_DIR.split(os.sep)[-1]
    image_root = os.sep.join([settings.BASE_DIR + settings.STATIC_URL + app_name, "images", file_name, file_name])

#    image_root = os.sep.join([base_dir + settings.STATIC_URL + app_name, "images", file_name, file_name])
    matchPath = glob.glob(image_root + ".*", recursive=True)

    return matchPath
