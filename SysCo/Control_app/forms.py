from django import forms
from django.forms import ModelForm
from .models import Gastos

class GastosForm(ModelForm):

    class Meta:
        model = Gastos
        fields = "__all__"
        exclude = []