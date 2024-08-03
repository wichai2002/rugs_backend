from rest_framework import viewsets

from subject.api.v1.serializers import SubjectModelSerializer
from subject.models import Subject

class SubjectModelViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectModelSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = []
    