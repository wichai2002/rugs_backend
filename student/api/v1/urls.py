from rest_framework import routers
from django.urls import path, include

from student.api.v1.views import StudentTermModelViewSet


router = routers.DefaultRouter()
router.register(r"term", StudentTermModelViewSet, basename="term")

urlpatterns = [
    path("", include(router.urls)),
]
