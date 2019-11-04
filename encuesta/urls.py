from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
        path('', views.pag_ppal, name = 'pag_ppal'),
	path('pag_ppal/contact_det/', views.contact_det, name = 'contact_det'),
	path('pag_ppal/desc_det/', views.desc_det, name = 'desc_det'),
	path('pag_ppal/app_encuesta/', login_required(views.app_encuesta), name = 'app_encuesta'),
	path('usuario/', views.welcome, name = 'welcome'),
	path('register', views.registrar_usr, name = 'register'),
	path('accounts/login/', views.login, name = 'login'),
	path('logout', views.logout, name = 'logout'),
]
