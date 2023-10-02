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

    return HttpResponse('vista inicio')

def cursos(request):

    return HttpResponse('vista cursos')

def profesores(request):

    return HttpResponse('vista profesores')

def estudiantes(request):

    return HttpResponse('vista estudiantes')

def entregables(request):

    return HttpResponse('vista entregables')