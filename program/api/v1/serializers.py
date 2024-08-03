from rest_framework import serializers
from django.db import transaction

from program.models import Program


class ProgramModelSeriliazers(serializers.ModelSerializer):
    
    class Meta:
        model = Program
        fields = [
            "id",
            "major",
            "detail",
            "version"
        ]