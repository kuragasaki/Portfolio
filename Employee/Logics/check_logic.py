#! Python3
# check_logic.py
from ..Forms.login_form import LoginForm
from ..models.login_model import LoginModel
from ..models.employee_model import EmployeeModel
from django.conf import settings
import matplotlib.pyplot as plt
import cv2 as openCV
import pathlib
import os
import shutil

# 事前設定
path_rel = pathlib.Path(settings.BASE_DIR + "/..")

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

# 顔認証チェック
# イメージファイルに顔が写っているかどうかをチェックする。
def check_face_image(file_path, file_name):
#    import pdb; pdb.set_trace()
    # イメージファイルの読み込み
    img = openCV.imread(file_path)
    if img is None:
        print("ファイル読み込み失敗")
        return False
    
    # 灰色変換(顔の識別しやすくするため)
    img_gray = openCV.cvtColor(img, openCV.COLOR_BGR2GRAY)

    # カスケードファイルの指定と顔検知器設定
    cascade = openCV.CascadeClassifier(str(path_rel.resolve()) + "/haarcascades/opencv-master/data/haarcascades/haarcascade_frontalface_alt.xml")
    
    # 顔認証
    facerect = cascade.detectMultiScale(img_gray)

    # 顔認証に一致しなかった場合
    if len(facerect) == 0:
        # 画像削除
        shutil.rmtree(file_path[:-len(file_name)])
        return False

    else:
        divide＿num = 1
        height = img.shape[0]
        width = img.shape[1]

        while height > 300 or width > 300:
            height = int(img.shape[0] * (10 - divide＿num) / 10)
            width = int(img.shape[1] * (10 - divide＿num) / 10)
            divide＿num += 1

        img_resize = openCV.resize(img, (width, height))
        openCV.imwrite(file_path, img_resize)

    return True