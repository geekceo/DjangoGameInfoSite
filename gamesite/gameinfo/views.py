from django.shortcuts import render

from .models import Genre

def index(request) -> render:
    return render(
        request,
        'gameinfo/index.html',
        {
            'title': 'Главная страница'
        }
    )

def showGenreGames(request, genreId) -> render:
    return render(
        request,
        'gameinfo/genre.html',
        {
            'title': Genre.objects.get(name=genreId).name_loc
        }
    )
