from django.test import TestCase
from django.core.files import File
from encuesta.models import Images

# Create your tests here.

image_path = '/home/vanessa/Escritorio/PISCIS_dic/media/image/par_glx_Nr_1.png'

class ImagesTest(TestCase):

    def test_basic_addition(self):
        imagen_prueba = Images()
        imagen_prueba.picture = File(open(image_path, 'rb'))
        imagen_prueba.save()
        
        p = Images.objects.get(id=1).picture.path
        
        self.failUnless(open(p), 'file not found')
