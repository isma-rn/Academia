from django.contrib import admin
from GestionAcademia.models import Afinidad,Grimorio,Estudiante,Estatus,Solicitud

@admin.register(Afinidad)
class AfinidadAdmin(admin.ModelAdmin):
    list_display=['id','nombre']

@admin.register(Grimorio)
class GrimorioAdmin(admin.ModelAdmin):
    list_display=['id','nombre']

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display=['id','nombre','apellido','identificacion', 'afinidad', 'grimorio']

@admin.register(Estatus)
class EstatusAdmin(admin.ModelAdmin):
    list_display=['id','nombre']

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display=['id','creacion','ultimaModificacion','estudiante', 'estatus']