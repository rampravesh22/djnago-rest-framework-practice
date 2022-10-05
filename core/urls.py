from django.urls import path
from core import views
urlpatterns = [
    path("student/",views.StudentAPI.as_view(),name="student")
]
