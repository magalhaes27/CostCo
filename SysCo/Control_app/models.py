from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# class Ingreso(models.Model):
#     montante = models.FloatField()  # DECIMAL
#     fecha = models.DateField(default=now)
#     descripcion = models.TextField()
#     usuario = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     finalidad = models.CharField(max_length=266)

#     def __str__(self):
#         return self.finalidad

#     class Meta:
#         ordering = ['-fecha']


# class Finalidad(models.Model):
#     nombre = models.CharField(max_length=255)

#     def __str__(self):
#         return self.nombre



class Gastos(models.Model):

    GATEGORIA = [
    ('AL','Alimentacion'),
    ('TRANSP','Transporte'),
    ('EST','Estudio'),
    ('EMP','Empleo'),
    ('ENT','Entretenimiento'),
    ('CS','Casa')]
    montante = models.FloatField()
    fecha = models.DateField(default=now)
    descripcion = models.TextField()
    categoria = models.CharField(max_length = 30,blank=True, choices=GATEGORIA, default="Casa")


    def __str__(self):
        return self.categoria

    class Meta:
        ordering = ['-fecha']


