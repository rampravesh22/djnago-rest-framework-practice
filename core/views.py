from core.models import Student
from django.http import JsonResponse
from core.serializers import StudentSerializer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        print(pythondata)
        print(id)
        if id is not None:
            print("id is not none", id)
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data)
    def post(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"yes": "The data is savee to database"})
        return JsonResponse(serializer.errors)
    def put(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        # complete upadae: required all data from front end/client
        # serializer = StudentSerializer(stu,data=pythondata)
        # partial update: all data not required
        serializer = StudentSerializer(stu, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg": "updated successfully"})
        else:
            return JsonResponse({'msg': "failed"})
    def delete(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        print(id)
        stu = Student.objects.get(id=id)
        x= stu.name
        stu.delete()
        return JsonResponse({'msg': "data deleted successfully","name":f"data is deleted with the name {x} "})

        
        
        
    
