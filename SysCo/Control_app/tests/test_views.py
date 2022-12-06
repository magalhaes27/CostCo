from django.test import TestCase, Client
from Control_app.models import Gastos
from django.urls import reverse
import json


class TestViews(TestCase):

    def setUp(self):
        self.cliente = Client()
        self.inicio_url = reverse('Control_app:inicio')

    def test_incio_listar(self):
        response = self.cliente.get(self.inicio_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'Control_app/inicio_gastos.html')

    