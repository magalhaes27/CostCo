# Register your models here.
from .models import Gastos
from django.contrib import admin
from django.contrib.sessions.models import Session

class GastoAdmin(admin.ModelAdmin):
    list_display = ('montante', 'descripcion', 'categoria', 'fecha',)
    search_fields = ('descripcion', 'categoria', 'fecha',)

    list_per_page = 5


admin.site.register(Gastos, GastoAdmin)