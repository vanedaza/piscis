# This file is part of the:
#   Piscis Project (https://github.com/mkoraj/piscis).
# Copyright (c) 2019 Koraj, Mauricio; Lares, Marcelo; Alfaro, Germán; Santucho,Victoria; Benavides,Jose & Daza, Ingrid All rights reserved.
# License: MIT License
#   Full Text: https://github.com/mkoraj/piscis/blob/master/LICENSE

from django import forms
from .models import *

class ImageForm(forms.ModelForm):
   class Meta:
      model = Imagen
      fields = ['image']
