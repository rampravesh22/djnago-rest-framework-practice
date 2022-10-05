from core.models import Student
from django.http import JsonResponse
from core.serializers import StudentSerializer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def student_api(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        print(pythondata)
        print(id)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JsonResponse(serializer.data, safe=False)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)
