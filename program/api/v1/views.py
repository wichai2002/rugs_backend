from rest_framework import viewsets

from program.models import Program
from program.api.v1.serializers import ProgramModelSeriliazers
from rest_framework.parsers import JSONParser


class ProgramModelViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramModelSeriliazers
    parser_classes = []
    http_method_names = ['get', 'post', 'patch', 'delete']
    parser_classes = [JSONParser]
    