from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client


class Test_ppal_views(TestCase):
    def test_inicio_renders(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)

    def test_contact_renders(self):
        response = self.client.get(reverse('contacto'))
        self.assertEqual(response.status_code, 200)

    def test_proyecto_renders(self):
        response = self.client.get(reverse('proyecto'))
        self.assertEqual(response.status_code, 200)






class TestDownloadView(TestCase):
    def test_anonymous_cannot_see_page(self):
        response = self.client.get('inicio/voto/')
        print(response)
        self.assertRedirects(response, 'accounts/iniciar_sesion/?next=inicio/voto/')

#    def test_authenticated_user_can_see_page(self):
#        user = User.objects.create_user("Juliana," "juliana@dev.io", "some_pass")
#        self.client.force_iniciar_sesion(user=user, token=user.auth_token)
#        response = self.client.post(reverse('voto'))
#        print(response)
#        self.assertEqual(response.status_code, 200)
        # Or assert you can see stuff on the page


