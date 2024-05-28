from django.db import models

# Create your models here.

class Afinidad(models.Model):
    nombre=models.CharField(max_length=20)

class Grimorio(models.Model):
    nombre=models.CharField(max_length=20)
    numeroHojas=models.IntegerField()

class Estudiante(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    identificacion=models.CharField(max_length=10)
    edad=models.IntegerField()
    afinidad=models.ForeignKey(Afinidad, on_delete=models.CASCADE)
    grimorio=models.ForeignKey(Grimorio, on_delete=models.CASCADE, blank=True, null=True)

class Estatus(models.Model):
    nombre=models.CharField(max_length=20)

class Solicitud(models.Model):
    creacion=models.DateTimeField()
    ultimaModificacion=models.DateTimeField(null=True,blank=True)
    estudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    estatus=models.ForeignKey(Estatus, on_delete=models.CASCADE)