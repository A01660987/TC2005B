from django.shortcuts import render
from django.http import JsonResponse
from tabla.models import Alumnos

# Create your views here.

def datos(request):
    datosdb = []
    for alumno in Alumnos.objects.all():
        datosdb.append({
            "nombre": alumno.nombre,
            "apellido": alumno.apellido,
            "horas": alumno.horas
        })
    return JsonResponse({"datos":datosdb})

def index(request):
    return render(request, 'tabla/index.html')