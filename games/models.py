from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=255)
    platform =  models.CharField(max_length=13, default="")
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

   

