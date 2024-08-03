from rest_framework import serializers
from django.db import transaction

from student.models import StudentTerm


class StudentTermModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTerm
        fields = [
            "id",
            "user",
            "gps",
            "subjects",
            "created_at"
        ]
    
    @transaction.atomic
    def create(self, validated_data):
        return super().create(validated_data)
    
    @transaction.atomic
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)