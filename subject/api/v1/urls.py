from rest_framework import routers
from django.urls import path, include

from subject.api.v1.views import SubjectModelViewSet


router = routers.DefaultRouter()
router.register(r"subject", SubjectModelViewSet, basename="subject")

urlpatterns = [
    path("", include(router.urls)),
]
