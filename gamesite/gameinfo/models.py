from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=255)
    decription = models.TextField()
    logo = models.ImageField(upload_to='gameinfo/images/', blank=True, null=True, verbose_name='Иконка')
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name