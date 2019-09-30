from django.db import models

# Create your models here.

   
class Choice(models.Model):

    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    CHOICE_TEXT = (('A', 'Alta'), ('B', 'Baja'))
    Que_tipo_de_interacción_ves = models.CharField(max_length=200, choices=CHOICE_TEXT, default='A')
    image = models.ImageField(upload_to= 'galaxias', default='galaxias/tailandia.jpg')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.Que_tipo_de_interacción_ves
    