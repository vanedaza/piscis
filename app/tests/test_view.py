# This file is part of the:
#   Piscis Project (https://github.com/mkoraj/piscis).
# Copyright (c) 2019 Koraj, Mauricio; Lares, Marcelo; Alfaro, Germán; Santucho,Victoria; Benavides,Jose & Daza, Ingrid All rights reserved.
# License: MIT License
#   Full Text: https://github.com/mkoraj/piscis/blob/master/LICENSE

from django.test import TestCase


class PisisViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/app/image_gallery/') 
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('images' in resp.context)
        self.assertTemplateUsed(resp, 'image_gallery.html')

