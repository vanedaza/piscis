from django.db import models
   
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


