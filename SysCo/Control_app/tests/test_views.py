from django.test import TestCase, Client
from Control_app.models import Gastos
from django.urls import reverse
import json


# Para hacer los tests de las vista se invoca la clase Client para servir de un servidor web para testar los métodos POST and GET.
class TestViews(TestCase):
#inicialización de las instancias para el testeo
    def setUp(self):
        self.cliente = Client()
        self.inicio_url = reverse('Control_app:inicio')
# test para listar los gastos
    def test_incio_listar(self):
        response = self.cliente.get(self.inicio_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'Control_app/inicio_gastos.html')

