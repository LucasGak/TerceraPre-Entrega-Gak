from django.urls import path, include
from AppCoder import views
from .views import *

urlpatterns = [
    path('', views.inicio),
    path('cursos/', cursos, name="cursos"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name="entregables"),

]