# Generated by Django 3.2.9 on 2021-12-03 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211203_0206'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movie',
            new_name='MovieList',
        ),
    ]