from django.db import models
from django.contrib.auth.models import User


class Choice(models.Model):
    """"For a uploaded image, allow select between three different types one to classify it"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE,  blank=True, null=True)
    cover = models.ImageField(upload_to='static/',  default = 'static/Scatter_Mh_vs_Ms.png')
    CHOICE_TEXT = (('A', 'Alta'), ('B', 'Baja'), ('C','Ninguna'))
    voto = models.CharField(max_length=200, choices=CHOICE_TEXT)
    
class Astronomer(models.Model):
    user = models.OneToOne(User, on_delete=models.CASCADE)
    name = models.charField()