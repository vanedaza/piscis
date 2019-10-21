# This file is part of the:
#   Piscis Project (https://github.com/mkoraj/piscis).
# Copyright (c) 2019-2020, PISCIS
# License: BSD-3-Clause
#   Full Text: https://github.com/mkoraj/piscis/blob/master/LICENSE

from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('image_gallery/', views.image_gallery, name='image_gallery')   
]

