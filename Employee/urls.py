from django.urls import path
from .views.login_view import LoginView
from .views.edit_view import EditView

urlpatterns = [
    path('', LoginView.as_view(), name='index'),
    path('index', LoginView.as_view()),
    path('top', LoginView.as_view()),
    path('login', LoginView.as_view(), name='login'),
#    path('view', views.login, name='view'),
    path('new', EditView.as_view(), name='new'),
    path('edit', EditView.as_view(), name='edit'),
#    path('search', views.login, name='search'),
#    path('logout', views.login, name='logout'),
#    path('確認画面', views.login, name='logout'),
]
