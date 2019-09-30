from django import forms
from .models import *

class Choice(forms.ModelForm):
   class Meta:
      model = Choice
      fields = ['image']