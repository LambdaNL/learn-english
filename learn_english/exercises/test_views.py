import json
from django.core.urlresolvers import reverse
from django.test import TestCase


class ViewsTests(TestCase):

    def setUp(self):
        pass

    def test_adverbs(self):
        url = "/adverbs/"
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
