from rest_framework.serializers import ModelSerializer
from GestionAcademia.models import Solicitud

class SolicitudSerializer(ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ['id','creacion','ultimaModificacion']