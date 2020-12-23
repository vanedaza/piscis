Models edit Tutorial
====================

This section contains a step-by-step tutorial with examples for config the **Models** that make up our 
*encuesta* (survey).


We show you how to configure the file models.py to use PISCIS in your research. Allowing you to choose the
images and the options that accompany them. Both make up the record of the answers that will be stored in
the database.

Load Django librarys


    .. code-block:: console 


        from django.contrib.auth.models import User
        from django.db import models

The **class Images** should not be edited unless you want to change the directory of images (edit "image").


    .. code-block:: console 

        class Images(models.Model):
            picture = models.ImageField(upload_to="image")


The PISCIS user must edit CHOICE_TEXT to configure the options to be voted on. These follow the configuration ('label save in .db', 'label show in web page')


    .. code-block:: console 

        class Choice(models.Model):

            usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
            imagen = models.ForeignKey(
                Images, on_delete=models.CASCADE, blank=True, null=True)

            CHOICE_TEXT = (("A", "Alta"), ("B", "Baja"), ("C", "Media"))
            voto = models.CharField(max_length=20, choices=CHOICE_TEXT)


