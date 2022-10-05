from django.urls import path
from core import views
urlpatterns = [
    path("student/",views.student_api,name="student")
]
