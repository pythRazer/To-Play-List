# Generated by Django 3.1.11 on 2021-05-24 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_game_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='aa',
            field=models.CharField(default='', max_length=255),
        ),
    ]
