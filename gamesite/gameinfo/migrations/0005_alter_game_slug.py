# Generated by Django 4.0.6 on 2022-07-08 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0004_game_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
