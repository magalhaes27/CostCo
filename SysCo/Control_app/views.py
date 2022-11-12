from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate ,logout
from django.contrib.auth import login as dj_login
from django.contrib.auth.models import User
from .models import AddPresupuesto_info,Perfil_Usuario
from django.contrib.sessions.models import Session
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from django.db.models import Sum
from django.http import JsonResponse
import datetime
from django.utils import timezone

# Create your views here.

def index(request):
    context_dict = {'text':'Bienvenido al Control de Gasto'}
    return render(request,'Control_app/base.html')