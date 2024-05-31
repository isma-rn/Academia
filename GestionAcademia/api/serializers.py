from rest_framework.serializers import ModelSerializer
from GestionAcademia.models import Solicitud

class SolicitudSerializer(ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'

class EstatusSerializer(ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ['estatus']