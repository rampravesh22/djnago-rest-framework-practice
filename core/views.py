from django.shortcuts import render
from core.models import Student
from django.http import JsonResponse
# Create your views here.


def home(request):
   student = list(Student.objects.values())
   return JsonResponse({'data':student})
