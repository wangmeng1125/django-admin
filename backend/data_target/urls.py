from rest_framework.routers import SimpleRouter
from .views import DataTargetModelViewSet

router = SimpleRouter()
router.register("api/data_target", DataTargetModelViewSet)

urlpatterns = []
urlpatterns += router.urls