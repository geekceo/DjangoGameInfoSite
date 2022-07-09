from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('genre/<str:genreId>/', showGenreGames, name='genre'),
    path('genre/<str:genreId>/<slug:gameSlug>', showGameInfo, name='game')
]

