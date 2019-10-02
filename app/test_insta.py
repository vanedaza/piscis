'''test en desarollo'''
'''
from django.test import TestCase
from .models import Choice,  Imagen

class ChoiceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Choice.objects.create(Que_tipo_de_interacción_ves='A')

    def test_Que_tipo_de_interacción_ves(self):
        choice=Choice.objects.get(id=1)
        field_label = choice._meta.get_field('Que_tipo_de_interacción_ves')
        self.assertEquals(field_label,'Que tipo de interacción ves')'''