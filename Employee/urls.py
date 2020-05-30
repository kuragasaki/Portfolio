from django.urls import path
from .views_dir.login_view import LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='index'),
    path('index', LoginView.as_view()),
    path('top', LoginView.as_view()),
    path('login', LoginView.as_view(), name='login'),
#    path('view', views.login, name='view'),
#    path('new', views.edit, name='new'),
#    path('edit', views.edit, name='edit'),
#    path('search', views.login, name='search'),
#    path('logout', views.login, name='logout'),
#    path('確認画面', views.login, name='logout'),
]