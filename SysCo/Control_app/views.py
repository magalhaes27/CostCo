from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from datetime import datetime
from calendar import month
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from .models import Gastos
from .forms import GastosForm


def inicio(request):
    gastos = Gastos.objects.all().order_by('-fecha')
    
    # total de gastos en el año 
    gasto_anual = gastos.filter(fecha__year = datetime.now().year)
    total_montante_ano = sum(gasto.montante for gasto in gasto_anual)

    #total de gastos en el més
    gasto_mensual = gastos.filter(fecha__month=datetime.now().month)
    total_montante_mes = sum(gasto.montante for gasto in gasto_mensual)

    contenido = {
        "gastos":gastos,
        "gasto_anual":gasto_anual,
        "gasto_mensual":gasto_mensual,
        "total_anual":total_montante_ano,
        "total_mensual":total_montante_mes,
    }

    return render(request, 'Control_app/inicio_gastos.html',contenido)

def add_gastos(request):
    
    gasto_form = GastosForm()
    if request.method == "POST":
        gasto_form = GastosForm(request.POST)
        if gasto_form.is_valid():
            gasto = gasto_form.save()
            gasto.save()
        return redirect("/")
    contenido = {"gasto_form": gasto_form}
    return render(request, 'Control_app/add_gastos.html',contenido)


def actualizar(request,id:int):

    gasto = get_object_or_404(Gastos,id=id)
    gasto_form = GastosForm(instance=gasto)

    if request.method == "POST":
        gasto_form = GastosForm(request.POST,instance=gasto)
        if gasto_form.is_valid():
         gasto.save()
        return redirect("/")
    contenido = {"gasto":gasto,"gasto_form":gasto_form}
    return render(request,"Control_app/actualizar_gasto.html",contenido)

def eliminar(request, id:int):
    gasto = get_object_or_404(Gastos,id=id)

    if request.method == "POST":
        gasto.delete()
        return redirect("/")

    contenido = {"gasto":gasto}
    return render(request, "Control_app/eliminar_gasto.html", contenido) 