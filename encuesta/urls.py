from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
                                       PasswordResetView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetCompleteView,
                                        )
# from .views import HomePageView
# from django.contrib.auth.decorators import login_required
# from django.views.generic.base import TemplateView # new


# path('pag_ppal/app_encuesta/', HomePageView.as_view(), name='imagen'),
urlpatterns = [
    path('', views.pag_ppal, name='pag_ppal'),
    path('pag_ppal/contact_det/', views.contact_det, name='contact_det'),
    path('pag_ppal/desc_det/', views.desc_det, name='desc_det'),
    path('pag_ppal/app_encuesta/', views.app_encuesta, name='app_encuesta'),
    #    path('pag_ppal/app_encuesta/',
    #          login_required(views.app_encuesta),
    #          name = 'app_encuesta'),
    path('usuario/', views.welcome, name='welcome'),
    path('register', views.registrar_usr, name='register'),
    path('accounts/login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate,
        name='activate'),
    url(r'^accounts/login/reset/$',
        PasswordResetView.as_view(template_name='registration/password_reset_from.html'),
        name='password_reset'),
    url(r'^accounts/login/reset/done/$',
        PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^accounts/reset/done/$',
        PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),
]
