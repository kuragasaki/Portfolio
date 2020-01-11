from django.urls import path
from . import views
from .account_edit import AccountEdit 
from .account_confirm import AccountConfirm

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('edit', AccountEdit.as_view(), name='edit'),
    path('confirm', AccountConfirm.as_view(), name='confirm'),
]
