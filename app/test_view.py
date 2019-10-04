from django.test import TestCase


class PisisViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/app/image_gallery/') 
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('images' in resp.context)
        self.assertTemplateUsed(resp, 'image_gallery.html')

