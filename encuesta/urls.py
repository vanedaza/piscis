from django.urls import path
from . import views

urlpatterns = [
        path('', views.pag_ppal, name = 'pag_ppal'),
	path('pag_ppal/contact_det/', views.contact_det, name= 'contact_det'),
	path('pag_ppal/desc_det/', views.desc_det, name= 'desc_det'),
	path('pag_ppal/app_encuesta/', views.app_encuesta, name= 'app_encuesta'),
#	path('pag_ppal/new', views.choice_new, name='choice_new'),
]
