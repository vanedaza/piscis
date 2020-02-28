from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import random
from .models import *

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('voto','imagen',)
    #def __init__(self, *args, **kwargs):
    #    super(ChoiceForm, self).__init__(*args, **kwargs)
    #    instance = getattr(self, 'instance', None)
    #    if instance and instance.pk:
    #        self.fields['imagen'].widget.attrs['readonly'] = True


class AstronomerForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico")
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2",]
        
