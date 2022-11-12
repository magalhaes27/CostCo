from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

#Create your models here.
SELEC_CATEGORIA = [
    ("Alimento","Alimento"),
    ("Viaje","Viaje"),
    ("Compras","Compras"),
    ("Necesidades","Necesidades"),
    ("Entretenimiento","Entretenimiento"),
    ("Otro","Otro")
 ]
ADD_GASTOS = [
     ("Gasto","Gasto"),
     ("Ingreso","Ingreso")
 ]
SELEC_PROFESION =[
    ("Trabajador","Trabajador"),
    ("Empresario","Empresario"),
    ("Estudiante","Estudiante"),
    ("Otro","Otro")
]
class AddPresupuesto_info(models.Model):
    usuario = models.ForeignKey(User,default = 1, on_delete=models.CASCADE)
    add_presupuesto = models.CharField(max_length = 10 , choices = ADD_GASTOS )
    cantidad = models.BigIntegerField()
    fecha = models.DateField(default = now)
    categoria = models.CharField( max_length = 20, choices = SELEC_CATEGORIA , default ='Food')
    class Meta:
        db_table='addpresupuesto'
        
class Perfil_Usuario(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    profesion = models.CharField(max_length = 10, choices=SELEC_PROFESION)
    ahorro = models.IntegerField( null=True, blank=True)
    ingreso = models.BigIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='Perfil_image',blank=True)
    def __str__(self):
       return self.usuario.username
