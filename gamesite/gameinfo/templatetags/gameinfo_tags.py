from django import template
from gameinfo.models import *
from django import forms

register = template.Library()

@register.inclusion_tag('gameinfo/inclusiontemps/genre_list.html')
def showGenreList(selectedId = None) -> dict:
    genres = dict(
        zip(
            [genre.name for genre in Genre.objects.all().order_by('id')],
            [genre.name_loc for genre in Genre.objects.all().order_by('id')]
        )
    )

    return { 'genres': genres, 'selected': '-' } if selectedId == None else { 'genres': genres, 'selected': Genre.objects.get(name_loc=selectedId).name }
   

@register.inclusion_tag('gameinfo/inclusiontemps/genre_info_games.html')
def showGenreGames(genreId: str) -> dict:
    games = Game.objects.filter(genre=genreId).order_by('name')
    return { 'games': games }

@register.inclusion_tag('gameinfo/inclusiontemps/game_info.html')
def showGameInfo(gameId: str, form: forms.Form, comments: dict) -> dict:
    game = Game.objects.get(name=gameId)
    return { 'game': game, 'form': form, 'comments': comments }