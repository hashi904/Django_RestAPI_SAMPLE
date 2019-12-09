from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from blog.urls import router as blog_router
from accounts.urls import router as user_router

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(user_router.urls)),
    url(r'^api/', include(blog_router.urls)),
]
