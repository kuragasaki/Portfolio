#! Python3
# login_model.py

from django.db import models as django_models

class LoginModel(django_models.Model):
    id = django_models.AutoField(primary_key = True)
    email = django_models.EmailField(unique=True, max_length = 200)
    password = django_models.CharField(max_length = 20)
#    created_at = django_models.DateTimeField(auto_now_add=True)
#    updated_at = django_models.DateTimeField(auto_now=True)
