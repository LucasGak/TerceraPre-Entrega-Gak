from django.urls import path, include
from AppCoder import views
from .views import *

urlpatterns = [
    path('', views.inicio),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('entregables', views.entregables),

]