from django.test import TestCase, Client
from django.urls import reverse
from http import HTTPStatus
from encuesta.forms import AstronomerForm
from django.contrib.auth.models import User

class TestStaticPages(TestCase):
    # Páginas que solo muestran un archivo ".html"
    def setUp(self):
        self.client = Client()

    def test_pag_inicio(self):
        # Verifica si el código responde
        url = reverse("inicio")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_pag_inicio2(self):
        # Verifica el template usado
        url = reverse("inicio")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "encuesta/inicio.html")

    def test_pag_inicio3(self):
        # Verifica el template muestre las palabras "Encuesta", "Iniciar seción", "registrate"
        url = reverse("inicio")
        response = self.client.get(url)
        self.assertContains(response, "Encuesta")
        self.assertContains(response, "iniciar_sesion")
        self.assertContains(response, "registrate")

    def test_pag_contacto(self):
        url = reverse("contacto")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_pag_contacto2(self):
        url = reverse("contacto")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "encuesta/contacto.html")

    def test_pag_proyecto(self):
        url = reverse("proyecto")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_pag_proyecto2(self):
        url = reverse("proyecto")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "encuesta/proyecto.html")




class TestRegitrarUsr(TestCase):
    # Páginas que solo muestran un archivo ".html"
    def setUp(self):
        self.client = Client() #lo usamos como un navegador artificial

    def test_registrar(self):
        form = AstronomerForm()


class TestIniciarSesion(TestCase):


    def test_redirect_if_not_logged_in(self):
        form = AstronomerForm(
            data={
                "username": "user",
                "email": "user@mp.com",
                "password1": "user1234",
                "password2": "user1234",
            }
        )
        form.save()
        
        response = self.client.post(reverse('iniciar_sesion'), {'username': 'user', 'password': 'user1234'}, follow=True)
        self.assertRedirects(response, reverse('inicio'))

