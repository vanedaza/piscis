from django.shortcuts import render
from .models import *
from .forms import ChoiceForm


def pag_ppal(request):
    return render(request, 'encuesta/pag_ppal.html',{})

def contact_det(request):
    return render(request, 'encuesta/contact_det.html',{})

def desc_det(request):
    return render(request, 'encuesta/desc_det.html',{})

def user(request):
    return render(request, 'encuesta/user.html',{})

def app_encuesta(request):
	form = ChoiceForm()
#	form.save()
	return render(request, 'encuesta/app_encuesta.html',{'form':form})


