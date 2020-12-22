from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Choice


class ChoiceForm(forms.ModelForm):
    """Ingresa la información del voto por el usuario
    y el id de la imagen elegida"""

    class Meta:
        model = Choice
        fields = (
            "voto",
            "imagen",
        )


class AstronomerForm(UserCreationForm):
    """Información del usuario"""

    email = forms.EmailField(label="Correo electrónico")

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]
