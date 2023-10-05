from django.shortcuts import render
from .models import *
from AppCoder.forms import BuscaCursoForm, CursoFormulario


def inicio(request):

    return render(request, "Appcoder/index.html")

def cursos(request):

    return render(request, "Appcoder/cursos.html")

def profesores(request):

    return render(request, "Appcoder/profesores.html")

def estudiantes(request):

    return render(request, "Appcoder/estudiantes.html")

def entregables(request):

    return render(request, "Appcoder/entregables.html")

def cursoFormulario(request):
      
      if request.method == 'POST':
      
            curso =  Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
 
            curso.save()
 
            return render(request, "AppCoder/padre.html")
 
      return render(request,"AppCoder/cursoFormulario.html")

def formulario_api(request):
    if request.method == "POST":
        
        miFormulario = CursoFormulario(request.POST) 

        if miFormulario.is_valid():
        
            informacion = miFormulario.cleaned_data
        
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
        
            curso.save()
            
            profesor = Profesor(nombre=informacion["profesor"])

            profesor.save()

            return render(request, "AppCoder/padre.html")

    else:
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/formulario_api.html", {"miFormulario": miFormulario})

def buscador_curso(request):
    if request.method == "POST":
        miFormulario = BuscaCursoForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])


            return render(request, "AppCoder/resultados_buscador.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(request, "AppCoder/buscador_curso.html", {"miFormulario": miFormulario})