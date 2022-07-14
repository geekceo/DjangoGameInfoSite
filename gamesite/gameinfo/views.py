from typing import Any
from django.views.generic import ListView
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

class GenreGames(ListView):
    model = Genre
    template_name = 'gameinfo/genre.html'
    context_object_name = 'genre'

    def get_context_data(self, **kwargs: Any) -> dict:
        genre = get_object_or_404(Genre, name=self.kwargs['genreId'])
        context = super().get_context_data(**kwargs)
        context['title'] = genre.name_loc
        context['selected_genre'] = genre.name_loc
        context['genre_id'] = genre.id
        print(context)

        return context

def showGameInfo(request, genreId, gameSlug) -> render:
    game = get_object_or_404(Game, slug=gameSlug)
    comments = Comment.objects.filter(game=game).order_by('-time_create')
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