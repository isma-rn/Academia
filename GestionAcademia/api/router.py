from rest_framework.routers import DefaultRouter
from GestionAcademia.api.views import SolicitudApiViewSet

router_post = DefaultRouter()
router_post.register(prefix='post', basename='post', viewset=SolicitudApiViewSet)