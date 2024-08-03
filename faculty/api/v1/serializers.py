from rest_framework import serializers
from django.db import transaction
from faculty.models import Faculty, Major



class FacultyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = [
            "id",
            "name"
        ]
        
    @transaction.atomic
    def create(self, validated_data):
        return super().create(validated_data)
    
    @transaction.atomic
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class MajorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = [
            "id",
            "faculty",
            "name",
            "subjects"
        ]
        
    @transaction.atomic
    def create(self, validated_data):
        return super().create(validated_data)
    
    @transaction.atomic
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
        