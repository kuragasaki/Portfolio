#! Python3
# check_logic.py
from ..Forms.login_form import LoginForm
from ..models.login_model import LoginModel
from ..models.employee_model import EmployeeModel
 
def check_login(loginForm):

    # DBからメールアドレス、パスワードを条件にレコードを取得
    login_model = LoginModel.objects.filter(email = loginForm["email"].data, password = loginForm["password"].data)

    # レコードが取得できない場合。
    if not login_model:
        return True

    # レコードが存在している。
    return False

# メールアドレス存在チェック
# （メールアドレスの入力チェックはformクラスが実施しているから、
#  ここでは実施しない。）
def check_mailaddress(mailaddress):

    # DBからメールアドレスを条件にレコードを取得
    emp_model = EmployeeModel.objects.filter(email = mailaddress)

    # レコードが取得できた。
    if emp_model:
        return True

    # 存在すれば、True
    return False
