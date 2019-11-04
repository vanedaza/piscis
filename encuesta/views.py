from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from .forms import ChoiceForm
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


def pag_ppal(request):
    return render(request, 'encuesta/pag_ppal.html',{})

def contact_det(request):
    return render(request, 'encuesta/contact_det.html',{})

def desc_det(request):
    return render(request, 'encuesta/desc_det.html',{})

def app_encuesta(request):
#	all_choices = models.Choice.objects.all()
#	image = random.choice(all_choices)
	if request.method == "POST":
		form = ChoiceForm(request.POST)
		if form.is_valid():
			choice = form.save(commit=False)
			choice.usuario = request.user
#			choice.cover = request.cover
			choice.save()
			return redirect('app_encuesta')
	else:
		form = ChoiceForm()
		return render(request, 'encuesta/app_encuesta.html',{'form':form})

def welcome(request):
    if request.user.is_authenticated:
        return render(request, 'encuesta/welcome.html')

    return redirect('login')


def registrar_usr(request):
   # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Creamos la nueva cuenta de usuario
            user = form.save()
            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('pag_ppal')

    form.fields['username'].help_text = None
    form.fields['password2'].help_text = None
    return render(request, 'encuesta/registrar_usr.html',{'form':form})

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)
            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('pag_ppal')

    return render(request, 'encuesta/login.html', {'form':form})

def logout(request):
    do_logout(request)
    return redirect('welcome')


#def astronomerregister(request):
#	if request.method == 'POST':
#		print('algo')
#	else:
#		print('request es get')
	
