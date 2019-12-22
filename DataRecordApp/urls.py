from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from blog.urls import router as blog_router
from accounts.urls import router as user_router
from fitbit.urls import router as fitbit_router
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(user_router.urls)),
    url(r'^api/', include(blog_router.urls)),
    url(r'^api/fitbit/', include(fitbit_router.urls)),
    url(r'^api/signin/', obtain_jwt_token),
    url(r'^api/', include('accounts.urls')),
]