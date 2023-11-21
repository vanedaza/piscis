from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Choice



class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['voto', 'imagen']
        widgets = {
            'voto': forms.RadioSelect(choices=Choice.CHOICE_TEXT),
        }
    
    def __init__(self, *args, **kwargs):
        super(ChoiceForm, self).__init__(*args, **kwargs)
        self.fields['voto'].initial = 'A'  # Establecer 'Alta' como valor predeterminado


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
