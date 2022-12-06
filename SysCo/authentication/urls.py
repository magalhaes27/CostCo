from .views import CadastroView
from django.urls import path

app_name = 'authentication'

urlpatterns = [
    path('cadastrar', CadastroView.as_view(), name='cadastrar')
]