# Generated by Django 4.1.5 on 2023-07-31 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('EUR', 'Euro'), ('UDS', 'Dollars'), ('RUB', 'Rubles')], default='RUB', max_length=3),
        ),
    ]