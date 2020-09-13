from django.urls import path
from .views.login_view import LoginView
from .views.edit_view import EditView
from .views.form_preview import FormPreview
from .views.complete import CompleteView
from .views.search_view import SearchView
from .views.game import GameView

urlpatterns = [
    path('', LoginView.as_view(), name='index'),
    path('index', LoginView.as_view()),
    path('top', LoginView.as_view()),
    path('login', LoginView.as_view(), name='login'),
    path('new', EditView.as_view(), name='new'),
    path('edit', EditView.as_view(), name='edit'),
    path('search', SearchView.as_view(), name='search'),
    path('preview', FormPreview.as_view(), name='preview'),
    path('complete', CompleteView.as_view(), name='complete'),
    path('game', GameView.as_view(), name='game'),
    path('game/<int:test_id>/', GameView.as_view(), name='game'),
]
