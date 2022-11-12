from django.urls import path, include
from Control_app import views

app_name = 'Control_app'

urlpatterns= [
    path('', views.index,name='index'),



]