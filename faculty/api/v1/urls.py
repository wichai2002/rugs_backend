from rest_framework import routers
from django.urls import path, include

from faculty.api.v1.views import MajorModelViewSet, FacultyModelViewSet


router = routers.DefaultRouter()
router.register(r'faculty', FacultyModelViewSet, basename="faculty")
router.register(r'major', MajorModelViewSet, basename="major")

urlpatterns = [
    path("", include(router.urls)),
]
