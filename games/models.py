from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class Game(models.Model):
   
    title = models.CharField(max_length=255)
    STATUS = (
        ('T', 'Toplay'),
        ('P', 'Progressing'),
        ('F', 'Finished'),
    )

    status = models.CharField(max_length=1, choices=STATUS, default='T')

    PLATFORM = (
        ('PS5', 'PS5'),
        ('PS4', 'PS4'),
        ('Switch', 'Switch'),
        ('Xbox One', 'Xbox One'),
        ('Xbox Series X', 'Xbox Series X'),
        ('PC', 'PC'),
        ('Other', 'Other'),
    )

    platform = models.CharField(max_length=13, choices=PLATFORM, default='PC')
    
    # platform =  models.CharField(max_length=13, default="")
    date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title

   

