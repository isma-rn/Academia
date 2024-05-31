from django.contrib import admin
from GestionAcademia.models import Solicitud

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display=['id','nombre', 'apellido','afinidad','identificacion','edad','grimoro','estatus','creacion','ultimaModificacion']