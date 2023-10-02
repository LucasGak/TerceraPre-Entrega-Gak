from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

# def curso(self):

#         curso = Curso(nombre="Desarrollo web", camada="19881")
#         curso.save()
#         documentoDeTexto = f"------->Curso: {curso.nombre} Camada: {curso.camada}"

#         return HttpResponse(documentoDeTexto)

def inicio(request):

    return render(request, "Appcoder/inicio.html")

def cursos(request):

    return render(request, "Appcoder/cursos.html")

def profesores(request):

    return render(request, "Appcoder/profesores.html")

def estudiantes(request):

    return render(request, "Appcoder/estudiantes.html")

def entregables(request):

    return render(request, "Appcoder/entregables.html")