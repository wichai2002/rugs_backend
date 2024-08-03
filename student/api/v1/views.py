from rest_framework import viewsets

from student.api.v1.serlializers import StudentTermModelSerializer
from student.models import StudentTerm

class StudentTermModelViewSet(viewsets.ModelViewSet):
    queryset = StudentTerm.objects.all()
    serializer_class = StudentTermModelSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = []
    