from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('leaderboard/global/', views.global_leaderboard, name='global_leaderboard'),
    path('leaderboard/game/<int:game_id>/', views.game_leaderboard, name='game_leaderboard'),
    path('popularity/', views.game_popularity, name='game_popularity'),
]
