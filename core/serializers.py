from rest_framework import serializers
from core.models import Student

class StudentSerializer(serializers.Serializer):
   name = serializers.CharField(max_length=100)
   
   def create(self, validated_data):
      return Student.create(**validated_data)