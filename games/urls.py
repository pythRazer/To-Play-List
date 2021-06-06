from django.urls import path
from .views import GameListView, GameDelete, GameAdd, GameEdit


urlpatterns = [
    path('', GameListView.as_view(), name='home'),
    path('add-a-game', GameAdd.as_view(),name='add'),
    path('<int:pk>/edit/', GameEdit.as_view(), name="edit"),
    path('<int:pk>/delete/', GameDelete.as_view(), name='delete')
]