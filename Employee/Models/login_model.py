#! Python3
# login_model.py

from django.db import models

class LoginModel(models.Model):
    email = models.EmailField(max_length = 200)
    password = models.CharField(max_length = 20)

    