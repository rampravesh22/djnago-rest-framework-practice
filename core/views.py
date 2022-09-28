# from django.shortcuts import render
from core.models import Student
from django.http import  JsonResponse
from core.serializers import StudentSerializer
from rest_framework.parsers import JSONParser


# Create your views here.
def home(request):
    student = Student.objects.get(id=1)
    serializer = StudentSerializer(student)
    return JsonResponse(serializer.data,safe=False)
