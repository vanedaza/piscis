from django.test import TestCase

from encuesta.models import Images, Choice

# Create your tests here.

# GOOGLEAR COMO TESTEAR EL VALOR DE ESTE TIPO DE CAMPO
#class ImagesTest(TestCase):

#    @classmethod
#    def setUpTestData(cls): # creo un objeto 
#        Images.objects.create(picture='imagen_test')
    
#    def test_id_image(self):
#        imagen=Images.objects.get(id=1)

#    def test_get_absolute_url(self):
#        imagen=Images.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
#        self.assertEquals(imagen.get_absolute_url(),'/encuesta/imagen/1')

        
class ChoiceTest(TestCase): #### EN DESARROLLO

    @classmethod
    def setUpTestData(cls):
        Choice.objects.create(imagen='imagen_test', voto = 'A') #debo crear el objeto imagen y definir las tuplas antes, me pa

    def test_voto_label(self):
        vote=Choice.objects.get(id=1)
        field_label = vote._meta.get_field('voto').verbose_name
        self.assertEquals(field_label,'vote')


    def test_first_name_max_length(self):
        vote=Choice.objects.get(id=1)
        max_length = vote._meta.get_field('voto').max_length
        self.assertEquals(max_length,200)



    def test_get_absolute_url(self):
        vote=Choice.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(vote.get_absolute_url(),'/encuesta/vote/1')