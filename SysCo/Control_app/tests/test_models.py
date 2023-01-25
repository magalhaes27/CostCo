
from django.test import TestCase, Client
from django.urls import reverse
from Control_app.models import Gastos


class ModelTesting(TestCase):

    def setUp(self):
        self.gastos = Gastos.objects.create( montante = 3000,descripcion = " para compras de la casa")

    def test_categoria_model(self):
        gasto_instance = self.gastos
        self.assertTrue(isinstance(gasto_instance, Gastos))
        self.assertEqual(str(gasto_instance), 'Casa')
