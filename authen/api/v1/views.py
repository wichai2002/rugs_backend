from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from authen.api.v1.serializers import UserModelSerializer

from authen.models import User


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = []
    