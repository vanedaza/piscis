from django.db import models
from django.contrib.auth.models import User


class Images(models.Model):
    picture = models.ImageField(upload_to='image')



class Choice(models.Model):

    """For a uploaded image, allow select between three different types one to classify it"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ForeignKey(Images, on_delete=models.CASCADE,  blank=True, null=True)
    CHOICE_TEXT = (('A', 'Alta'), ('B', 'Baja'), ('C','Media'))    
    voto = models.CharField(max_length=200, choices=CHOICE_TEXT)
    
