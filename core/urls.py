from django.urls import path
from core import views
urlpatterns = [
    path("student/",views.home,name="home")
]
