# Generated by Django 3.1.3 on 2020-12-16 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_favoritesattraction_favoritesposterevent_favoritesrestaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoritesposterevent',
            name='obj',
        ),
        migrations.RemoveField(
            model_name='favoritesposterevent',
            name='user',
        ),
        migrations.RemoveField(
            model_name='favoritesrestaurant',
            name='obj',
        ),
        migrations.RemoveField(
            model_name='favoritesrestaurant',
            name='user',
        ),
        migrations.DeleteModel(
            name='FavoritesAttraction',
        ),
        migrations.DeleteModel(
            name='FavoritesPosterEvent',
        ),
        migrations.DeleteModel(
            name='FavoritesRestaurant',
        ),
    ]