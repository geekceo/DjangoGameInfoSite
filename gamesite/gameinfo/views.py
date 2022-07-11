from django.shortcuts import get_object_or_404, redirect, render

from .forms import *

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
    comments = Comment.objects.filter(game=game)
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            try:
                form.cleaned_data['game'] = game
                Comment.objects.create(**form.cleaned_data)
                return redirect(request.path)
            except:
                form.add_error(None, 'Ошибка добавления комментария')
    else:
        form = AddCommentForm()
    return render(
        request,
        'gameinfo/game.html',
        {
            'form': form,
            'title': game.name,
            'selected_genre': game.genre.name_loc,
            'game': game,
            'comments': comments
        }
    )