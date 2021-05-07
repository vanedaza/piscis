from django.conf.urls import url
from django.contrib.auth.views import (
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import path

from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("inicio/contacto/", views.contacto, name="contacto"),
    path("inicio/proyecto/", views.proyecto, name="proyecto"),
    path("inicio/voto/", views.voto, name="voto"),
    path("usuario/", views.welcome, name="welcome"),
    path("register", views.registrar_usr, name="register"),
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
    url(
        r"^accounts/iniciar_sesion/reset/$",
        PasswordResetView.as_view(
            template_name="registration/password_reset_from.html"
        ),
        name="password_reset",
    ),
    url(
        r"^accounts/iniciar_sesion/reset/done/$",
        PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done.html" 
        ),
        name="password_reset_done",
    ),
    url(
        r"^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]"
        + r"{1,13}-[0-9A-Za-z]{1,20})/$",
        PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    url(
        r"^accounts/reset/done/$",
        PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
