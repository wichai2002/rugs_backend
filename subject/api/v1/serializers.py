from rest_framework import serializers
from django.db import transaction

from subject.models import Subject


class SubjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = [
            "id",
            "name",
            "code",
            "unit",
            "created_at"
        ]
    
    @transaction.atomic
    def create(self, validated_data):
        return super().create(validated_data)
    
    @transaction.atomic
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)