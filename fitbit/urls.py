from rest_framework import routers
from .views import HourStepsViewSet


router = routers.DefaultRouter()
router.register(r'hoursteps', HourStepsViewSet)
