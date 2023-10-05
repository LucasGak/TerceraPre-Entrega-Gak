from django.urls import path
from AppCoder import views
from .views import *

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('cursos/', cursos, name="cursos"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name="entregables"),
    path('cursoFormulario/', views.cursoFormulario, name="cursoFormulario"),
    path('formulario_api/', views.formulario_api, name="formulario_api"),
    path('buscador_curso/', views.buscador_curso, name="buscador_curso"),

]