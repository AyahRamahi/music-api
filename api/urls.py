from django.urls import path, include
from rest_framework import routers
from . import views


# rest framework handles requests with viewsets using routers
# define router and register your viewset
router = routers.DefaultRouter()
router.register('', views.IndexViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
