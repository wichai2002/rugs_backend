from rest_framework import viewsets

from faculty.api.v1.serializers import FacultyModelSerializer, MajorModelSerializer
from faculty.models import Faculty, Major


class FacultyModelViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultyModelSerializer
    permission_classes = []
    http_method_names = ['get', 'post', 'patch', 'delete']
    
    
class MajorModelViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorModelSerializer
    permission_classes = []
    http_method_names = ['get', 'post', 'patch', 'delete']
    