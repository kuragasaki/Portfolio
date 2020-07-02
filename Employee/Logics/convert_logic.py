#! Python3
# convert_logic.py

from ..Forms.login_form import LoginForm
from ..Forms.employee_form import EmployeeForm
from ..models.employee_model_form import EmployeeModelForm


def employeeFormToDict(param_name_list, empForm):
    view_map = {}
    for param_name in param_name_list:
        view_map[param_name] = empForm[param_name].data

    return view_map


def employeeModelToDict(empModel):
    result_list = []
    for param in empModel:
        result = {
            "name": param.name
            , "email": param.email
            , "password": "セキュリティの観点から入力された値は表示されません。"
            , "gender": "男性" if param.gender == "0" else "女性"
            , "date_of_joining": param.date_of_joining
            , "retirement_date": param.retirement_date
            , "user_img": param.user_img
            , "admin_num": "管理職" if param.admin_num else "社員"
        }

        result_list.append(result)

    return result_list

def employeeModelToModelForm(empModel):
    """
    emp_model_form = EmployeeModelForm(
        name = empModel.name
        , email = empModel.email
        , password = empModel.password
        , gender = empModel.gender
        , date_of_joining = empModel.date_of_joining
        , retirement_date = empModel.retirement_date
        , user_img = empModel.user_img
        , admin_num = empModel.admin_num
    )
    """

    result = {
        "name": empModel.name
        , "email": empModel.email
        , "password": empModel.password
        , "gender": empModel.gender
        , "date_of_joining": empModel.date_of_joining
        , "retirement_date": empModel.retirement_date
        , "user_img": empModel.user_img
        , "admin_num": empModel.admin_num
    }

    emp_model_form = EmployeeModelForm(initial = result)

    return emp_model_form
