from django.test import TestCase
from django.core.files import File
from encuesta.models import Images, Choice
from django.contrib.auth.models import User

# Create your tests here.

image_path = "media/" + "image/par_glx_Nr_1.png"


class ImagesTest(TestCase):
    def test_basic_addition(self):
        imagen_prueba = Images()
        imagen_prueba.picture = File(open(image_path, "rb"))
        imagen_prueba.save()

        p = Images.objects.get(id=1).picture.path

        
        self.failUnless(open(p), 'file not found')


class ChoiceTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User()
        user.save()
        imagen_prueba = Images()
        imagen_prueba.picture = File(open(image_path, 'rb'))
        imagen_prueba.save()
        CHOICE_TEXT = "A"
        Choice.objects.create(usuario=user, imagen=imagen_prueba, voto=CHOICE_TEXT)

    def test_voto(self):
        choice = Choice.objects.get(id=1)
        self.assertEqual(choice.voto, "A") 

