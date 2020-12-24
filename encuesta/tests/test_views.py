from django.contrib.auth.models import User
from django.core.files import File
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from encuesta.forms import AstronomerForm
from encuesta.models import Images


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
        # El template muestra "Encuesta", "Iniciar seción", "registrate"
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


class TestVotePages(TestCase):
    @classmethod
    # Páginas que solo muestran un archivo ".html"
    def setUpTestData(clf):
        clf.request_factory = RequestFactory()
        image_path = "media/" + "image/par_glx_Nr_1.png"
        imagen_prueba = Images()
        imagen_prueba.picture = File(open(image_path, "rb"))
        clf.user = User.objects.create(
            username="javed",
            email="javed@javed.com",
            password="fsdfdsmy_secret",
        )

    def test_voto_get_usuario_logg(clf):
        request = clf.request_factory.get(reverse("voto"))
        request.user = clf.user
        clf.assertTemplateUsed("encuesta/voto.html")


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

        response = self.client.post(
            reverse("iniciar_sesion"),
            {"username": "user", "password": "user1234"},
            follow=True,
        )
        self.assertRedirects(response, reverse("inicio"))

    def test_render_not_logg(self):
        self.client = Client()
        url = reverse("iniciar_sesion")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "encuesta/iniciar_sesion.html")


class TestWelcomePage(TestCase):
    def setUp(self):
        self.client = Client()

    def test_pag_welcome_login(self):
        # Verifica si la pagina responde a un usuario loggeado
        c = Client()
        user = User()
        user.save()
        c.force_login(user)
        url = reverse("welcome")
        response = c.get(url)
        self.assertEqual(response.status_code, 200)


class TestLogOut(TestCase):
    # Páginas que solo muestran un archivo ".html"
    def setUp(self):
        self.client = Client()

    def test_log_out(self):
        # Verifica si el código responde
        url = reverse("logout")
        response = self.client.get(url)
        self.assertRedirects(response, "/usuario/", target_status_code=302)


class TestDownloadView(TestCase):
    def test_anonymous_cannot_see_page(self):
        response = self.client.get('inicio/voto/')
        print(response)
        self.assertRedirects(response, 'accounts/iniciar_sesion/?next=inicio/voto/')
