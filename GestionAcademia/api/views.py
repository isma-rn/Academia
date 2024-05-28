from rest_framework.viewsets import ModelViewSet
from GestionAcademia.models import Solicitud
from GestionAcademia.api.serializers import SolicitudSerializer

class SolicitudApiViewSet(ModelViewSet):
    serializer_class = SolicitudSerializer
    queryset = Solicitud.objects.all()