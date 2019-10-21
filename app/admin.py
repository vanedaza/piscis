# This file is part of the:
#   Piscis Project (https://github.com/mkoraj/piscis).
# Copyright (c) 2019-2020, PISCIS
# License: BSD-3-Clause
#   Full Text: https://github.com/mkoraj/piscis/blob/master/LICENSE

from django.contrib import admin
from .models import Choice
# Register your models here.


#admin.site.register(Question)
admin.site.register(Choice)
