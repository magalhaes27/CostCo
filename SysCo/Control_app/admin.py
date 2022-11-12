# Register your models here.
from .models import AddPresupuesto_info, Perfil_Usuario
from django.contrib import admin
from django.contrib.sessions.models import Session

class AddPresupuesto_infoAdmin(admin.ModelAdmin):
    list_display=("usuario","cantidad","fecha","categoria","add_presupuesto")

admin.site.register(AddPresupuesto_info,AddPresupuesto_infoAdmin)
admin.site.register(Session)
admin.site.register(Perfil_Usuario)
