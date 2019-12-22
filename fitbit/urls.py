from rest_framework import routers
from .views import HourStepsViewSet, HourStepsSearchViewSet


router = routers.DefaultRouter()
router.register(r'hoursteps/filter', HourStepsSearchViewSet)
router.register(r'hoursteps', HourStepsViewSet)

