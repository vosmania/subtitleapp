# Generated by Django 3.2.9 on 2021-12-03 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211203_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='core.GenreChoices'),
        ),
    ]
