# Generated by Django 3.1.11 on 2021-05-24 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_game_aa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='aa',
        ),
    ]
