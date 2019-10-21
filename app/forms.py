# This file is part of the:
#   Piscis Project (https://github.com/mkoraj/piscis).
# Copyright (c) 2019-2020, PISCIS
# License: BSD-3-Clause
#   Full Text: https://github.com/mkoraj/piscis/blob/master/LICENSE

from django import forms
from .models import *

class ImageForm(forms.ModelForm):
   class Meta:
      model = Imagen
      fields = ['image']
