from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, AuthRegister

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'signup/', AuthRegister.as_view()),
]