# Generated by Django 4.0.6 on 2022-07-06 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('decription', models.TextField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='gameinfo/images/', verbose_name='Иконка')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gameinfo.genre')),
            ],
        ),
    ]
