from django.db import models
from django.urls import reverse




class Character(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    acupation = models.CharField(max_length=100)
    planet = models.CharField(max_length=100)
    first_appearance = models.CharField(max_length=300)
    status = models.CharField(max_length=150, default='default value')
    img = models.ImageField(upload_to="character", null=True)
    
    def __str__(self):
        return self.name

class Episodes(models.Model):
   name = models.CharField(max_length=255)
   air_date = models.DateField()
   episode = models.CharField(max_length=255)
   characters = models.ManyToManyField(Character)  #('Character', related_name='episodes')