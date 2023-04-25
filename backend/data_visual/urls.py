from rest_framework.routers import SimpleRouter
from .views import DataVisualModelViewSet

router = SimpleRouter()
router.register("api/data_visual", DataVisualModelViewSet)

urlpatterns = []
urlpatterns += router.urls