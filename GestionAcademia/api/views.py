from rest_framework import  mixins, viewsets
from GestionAcademia.models import Solicitud
from GestionAcademia.api.serializers import SolicitudSerializer,EstatusSerializer

class SolicitudApiViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = SolicitudSerializer
    queryset = Solicitud.objects.all()
    http_method_names = ["get","put","post","delete"]

class EstatusViewSet(viewsets.ModelViewSet):
    serializer_class = EstatusSerializer
    queryset = Solicitud.objects.all()
    http_method_names = ["patch"]
    