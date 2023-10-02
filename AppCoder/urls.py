from django.urls import path, include
from AppCoder import views
from .views import inicio, cursos, profesores, estudiantes, entregables

urlpatterns = [
    path('', views.inicio),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('entregables', views.entregables),
    path('cursos/', cursos),
    path('AppCoder/', include('AppCoder.urls')),
]
