from rest_framework import routers
from django.urls import path, include

from program.api.v1.views import ProgramModelViewSet


router = routers.DefaultRouter()
router.register(r'', ProgramModelViewSet, basename="program")

urlpatterns = [
    path("", include(router.urls)),
]
