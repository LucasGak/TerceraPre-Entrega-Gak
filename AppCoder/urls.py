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

# from .views import saludo, muestra_template, probando_template, curso
# path('saludo/', saludo),
# path('muestra_nombre/<nombre>/', muestra_nombre),
# path('probando_template/', probando_template),
# path('usando_loader/', usando_loader),
# path('curso/<nombre>/<numero>/', curso),