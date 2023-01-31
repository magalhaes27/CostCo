from django.urls import path, include
from Control_app import views

app_name = 'Control_app'

urlpatterns= [
    path('', views.inicio,name='inicio'),
    path('adicionar/', views.add_gastos, name='adicionar'),
    path('actualizar/<str:id>',views.actualizar, name='actualizar'),
    path('eliminar/<str:id>',views.eliminar,name="eliminar")




]