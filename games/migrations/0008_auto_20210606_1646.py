# Generated by Django 3.1.11 on 2021-06-06 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_auto_20210606_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='platform',
            field=models.CharField(choices=[('PS5', 'PS5'), ('PS4', 'PS4'), ('Switch', 'Switch'), ('Xbox One', 'Xbox One'), ('Xbox Series X', 'Xbox Series X'), ('PC', 'PC'), ('Other', 'Other')], default='PC', max_length=13),
        ),
    ]
