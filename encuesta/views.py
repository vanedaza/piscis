from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from .forms import ChoiceForm, AstronomerForm
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
import random
from django.template import RequestContext, Context
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse

#from django.views.generic import ListView
#class HomePageView(ListView):
#    model = Images
#    template_name = 'encuesta/app_encuesta.html'

def pag_ppal(request):
    return render(request, 'encuesta/pag_ppal.html',{})

def contact_det(request):
    return render(request, 'encuesta/contact_det.html',{})

def desc_det(request):
    return render(request, 'encuesta/desc_det.html',{})

import copy 

def app_encuesta(request):
    pks = Images.objects.values_list('pk', flat=True) # flat=True will remove the tuples and return the list 
    random_idx = random.randint(1, len(pks))
    m = copy.copy(random_idx - 1)
    if request.method == "GET":
        prueba = list(Images.objects.all())

    if request.method == "POST":        
        form = ChoiceForm(request.POST)         #construir el PostForm con datos del voto
        if form.is_valid():                     #verifica si todos los datos son correctos
            choice = form.save(commit=False)    #commit=False significa que no queremos guardar el modelo Choice, primero queremos guardar lo que sigue
            choice.usuario = request.user
            choice.imagen = Images.objects.get(pk=pks[m])   #guardamos el formulario
            choice.save()                       #conservará los cambios (autor,voto,imagen) y se creará una nuevo objeto
            return redirect('app_encuesta')
    else:
        form = ChoiceForm()
    return render(request, 'encuesta/app_encuesta.html', {'form': form, 'prueba_images': prueba[m]}) 
     
def welcome(request):
    if request.user.is_authenticated:
        return render(request, 'encuesta/welcome.html')

    return redirect('login')

def registrar_usr(request):
    if request.method == "POST":
        form = AstronomerForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_activate = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activa tu cuenta de PISCIS.'
            message = render_to_string('encuesta/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        email_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Por favor confirme su cuenta de mail para completar el registro')
            if user is not None:
                do_login(request, user)
                return redirect('pag_ppal')
    else:
        form = AstronomerForm()
    form.fields['username'].help_text = None
    form.fields['password2'].help_text = None
    return render(request, 'encuesta/registrar_usr.html',{'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        do_login(request, user)
        # return redirect('home')
#        return HttpResponse('Gracias por confirmar su correo. Ahora puedes acceder a tu cuenta.')
        return redirect('app_encuesta')
    else:
        return HttpResponse('Link de activación invalido!')

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('pag_ppal')

    return render(request, 'encuesta/login.html', {'form':form})

def logout(request):
    do_logout(request)
    return redirect('welcome')

