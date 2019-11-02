from django import forms

from .models import *

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('voto',)

class AstronomerForm(form.ModelForm):
    class Meta:
        model = Astronomer
        