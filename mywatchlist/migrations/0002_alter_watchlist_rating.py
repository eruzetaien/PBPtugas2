# Generated by Django 4.1 on 2022-09-18 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='rating',
            field=models.FloatField(),
        ),
    ]