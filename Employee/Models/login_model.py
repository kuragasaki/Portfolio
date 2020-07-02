#! Python3
# login_model.py

from django.db import models as django_models

class LoginModel(django_models.Model):
    email = django_models.EmailField(unique=True, max_length = 200)
    password = django_models.CharField(max_length = 20)

    