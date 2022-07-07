from django import template
from gameinfo.models import *

register = template.Library()

@register.inclusion_tag('gameinfo/inclusiontemps/genre_list.html')
def showGenreList():
    genres = dict(
        zip(
            [genre.name for genre in Genre.objects.all().order_by('id')],
            [genre.name_loc for genre in Genre.objects.all().order_by('id')]
        )
    )

    return {'genres': genres}