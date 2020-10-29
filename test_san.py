from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client


class Test_ppal_views(TestCase):
    def test_pag_ppal_renders(self):
        response = self.client.get(reverse('pag_ppal'))
        self.assertEqual(response.status_code, 200)

    def test_contact_renders(self):
        response = self.client.get(reverse('contact_det'))
        self.assertEqual(response.status_code, 200)

    def test_desc_det_renders(self):
        response = self.client.get(reverse('desc_det'))
        self.assertEqual(response.status_code, 200)






class TestDownloadView(TestCase):
    def test_anonymous_cannot_see_page(self):
        response = self.client.get('pag_ppal/app_encuesta/')
        print(response)
        self.assertRedirects(response, 'accounts/login/?next=pag_ppal/app_encuesta/')

#    def test_authenticated_user_can_see_page(self):
#        user = User.objects.create_user("Juliana," "juliana@dev.io", "some_pass")
#        self.client.force_login(user=user, token=user.auth_token)
#        response = self.client.post(reverse('app_encuesta'))
#        print(response)
#        self.assertEqual(response.status_code, 200)
        # Or assert you can see stuff on the page


