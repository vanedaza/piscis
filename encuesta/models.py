from django.contrib.auth.models import User
from django.db import models


class Images(models.Model):
    picture = models.ImageField(upload_to="image")


class Choice(models.Model):
    """For a uploaded image, allow select between three different
    types one to classify it"""

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    imagen = models.ForeignKey(
        Images, on_delete=models.CASCADE, blank=True, null=True
    )
    CHOICE_TEXT = (("A", "Alta"), ("C", "Media"), ("B", "Baja"))
    voto = models.CharField(max_length=20, choices=CHOICE_TEXT)
