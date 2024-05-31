from rest_framework.routers import DefaultRouter
from GestionAcademia.api.views import SolicitudApiViewSet,EstatusViewSet

router_post = DefaultRouter()
router_post.register(prefix='solicitud', basename='solicitud', viewset=SolicitudApiViewSet)
router_post.register(prefix='solicitudEstatus', basename='solicitudEstatus', viewset=EstatusViewSet)