from django.conf.urls import url
from django.contrib.auth.views import (
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.urls import path

from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("inicio/contacto/", views.contacto, name="contacto"),
    path("inicio/proyecto/", views.proyecto, name="proyecto"),
    path("inicio/voto/", views.voto, name="voto"),
    path("usuario/", views.welcome, name="welcome"),
    #path("register", views.registrar_usr, name="register"),
    path("inicio/activar_correo/", views.registrar_usr, name="register"),
    path(
        "accounts/iniciar_sesion/", views.iniciar_sesion, name="iniciar_sesion"
    ),
    path(
        "accounts/login/", views.login, name="login"
    ),
    path("logout", views.logout, name="logout"),
    url(
        r"^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/"
        + r"(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$",
        views.activate,
        name="activate",
    ),
    # change password urls
    path('password_change/', PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(),name='password_change_done'),
    # reset password urls
    path('password_reset/',
        PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
        name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="registration/password_change_form.html"),name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
