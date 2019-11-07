from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('voto',)


class AstronomerForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico")
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2",]
        
