from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet
from django.contrib import admin

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
