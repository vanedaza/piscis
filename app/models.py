from django.db import models
   
class Imagen(models.Model):
    image = models.ImageField(upload_to = 'app', default = 'app/static/galaxias/img1.jpeg')
    name = models.CharField(max_length=200)

class Choice(models.Model):
    imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE,  blank=True, null=True)
    CHOICE_TEXT = (('A', 'Alta'), ('B', 'Baja'), ('C','Ninguna'))
    Que_tipo_de_interacción_ves = models.CharField(max_length=200, choices=CHOICE_TEXT, default='A')
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.Que_tipo_de_interacción_ves


