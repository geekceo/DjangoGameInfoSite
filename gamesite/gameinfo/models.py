from pickle import FALSE
from django.db import models
from django.urls import reverse

class Game(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    decription = models.TextField()
    logo = models.ImageField(upload_to='gameinfo/images/', blank=True, null=True, verbose_name='Иконка')
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)
    developer = models.CharField(max_length=255)
    

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('game', kwargs={'genreId': self.genre.name, 'gameSlug': self.slug})


class Genre(models.Model):
    name = models.CharField(max_length=255)
    name_loc = models.CharField(max_length=255, default='default')

    def __str__(self) -> str:
        return self.name