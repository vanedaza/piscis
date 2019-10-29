# This file is part of the:
#   Piscis Project (https://github.com/mkoraj/piscis).
# Copyright (c) 2019 Koraj, Mauricio; Lares, Marcelo; Alfaro, Germán; Santucho,Victoria; Benavides,Jose & Daza, Ingrid All rights reserved.
# License: MIT License
#   Full Text: https://github.com/mkoraj/piscis/blob/master/LICENSE

from django.db import models
from django.contrib.auth.models import User
   
class Imagen(models.Model):
    """"Upload the image to be voted. The uploaded images are saved in a gallery"""
    image = models.ImageField(upload_to = 'app', default = 'app/static/galaxias/img1.jpeg')
    name = models.CharField(max_length=200)

class Choice(models.Model):
    """"For a uploaded image, allow select between three different types one to classify it"""
    imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE,  blank=True, null=True)
    CHOICE_TEXT = (('A', 'Alta'), ('B', 'Baja'), ('C','Ninguna'))
    Que_tipo_de_interacción_ves = models.CharField(max_length=200, choices=CHOICE_TEXT)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.Que_tipo_de_interacción_ves

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="Usuario", on_delete=models.CASCADE, primary_key=True)
    Choice_genre = (('m', 'Masculino'), ('f', 'Feminino'),('o', 'Otro'))
    website=models.URLField(default='', null=True)
    genre = models.CharField(max_length=1, choices=Choice_genre)
    birth_date = models.DateField(default='', null=True)
    def __str__(self):
        return str(self.user)

