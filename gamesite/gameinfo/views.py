from django.shortcuts import render

from .models import Genre, Game

def index(request) -> render:
    return render(
        request,
        'gameinfo/index.html',
        {
            'title': 'Главная страница',
            'selected_genre': '-'
        }
    )

def showGenreGames(request, genreId) -> render:
    return render(
        request,
        'gameinfo/genre.html',
        {
            'title': Genre.objects.get(name=genreId).name_loc,
            'genreId': Genre.objects.get(name=genreId).id,
            'selected_genre': Genre.objects.get(name=genreId).name_loc
        }
    )

def showGameInfo(request, genreId, gameId) -> render:
    return render(
        request,
        'gameinfo/game.html',
        {
            'title': gameId,
            'selected_genre': Genre.objects.get(name=genreId).name_loc,
            'game': Game.objects.get(name=gameId)
        }
    )