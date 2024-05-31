from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Solicitud(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    afinidad=models.CharField(max_length=20)
    identificacion=models.CharField(max_length=10)
    edad=models.IntegerField(validators=[
            MaxValueValidator(99),
            MinValueValidator(1)
        ])    
    grimoro=models.CharField(null=True,blank=True,max_length=20)
    estatus=models.CharField(max_length=20,default="creado")
    creacion=models.DateTimeField()
    ultimaModificacion=models.DateTimeField(null=True,blank=True)