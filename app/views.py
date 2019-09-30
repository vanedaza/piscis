from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    return HttpResponse("Bienvenidos a la app de PISCIS")


def upload_image(request):
   if request.method == 'GET':
      return render(request, 'upload_image.html')
   elif request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = Choice(image = form.cleaned_data["image"])
            new_image.save()
            return HttpResponseRedirect('/app/image_gallery/')

def upload_image(request):
    if request.method == 'GET':
        return render(request, 'upload_image.html')

def image_gallery(request):
    images = Choice.objects.all()
    print(images)
    return render(request, 'image_gallery.html', {'images': images})
    