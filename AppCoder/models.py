from django.db import models

#Creados los modelos curso, estudiante, profesor y entregable

class Curso(models.Model):

    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()
    
class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()

class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)

class Entregable(models.Model):
    nombre=models.CharField(max_length=30)
    FechaDeEntrega=models.DateField()
    entregado=models.BooleanField()