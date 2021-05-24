from django.urls import path
from .views import GameListView, GameDelete


urlpatterns = [
    path('', GameListView.as_view(), name='home'),
    path('<int:pk>/delete/', GameDelete.as_view(), name='delete')
]