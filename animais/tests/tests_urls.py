from django.http import response
from django.test import TestCase, RequestFactory
from django.urls import reverse
from animais.views import index


class AnimaisURLSTestCase (TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_url_view_utiliza_index(self):
        """Testa se a home da aplicação utiliza o função index"""
        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code,200)
