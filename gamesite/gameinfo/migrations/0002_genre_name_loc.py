# Generated by Django 4.0.6 on 2022-07-07 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='name_loc',
            field=models.CharField(default='default', max_length=255),
        ),
    ]
