from django.shortcuts import get_object_or_404, render

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
    genre = get_object_or_404(Genre, name=genreId)
    return render(
        request,
        'gameinfo/genre.html',
        {
            'title': genre.name_loc,
            'genreId': genre.id,
            'selected_genre': genre.name_loc
        }
    )

def showGameInfo(request, genreId, gameSlug) -> render:
    game = get_object_or_404(Game, slug=gameSlug)
    return render(
        request,
        'gameinfo/game.html',
        {
            'title': game.name,
            'selected_genre': game.genre.name_loc,
            'game': game
        }
    )