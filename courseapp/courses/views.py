from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets, permissions
from .models import Course, Category
from .serializers import CourseSerializer, CategorySerializer
from .paginators import CoursePagination

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active = True)
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = CoursePagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




# Create your views here.
def index(request):
    return render(request, template_name="adminpage.html", context={'name':'admin'})

def welcome(request, year):
    return HttpResponse("Hello " + str(year))

def welcome2(request, year):
    return HttpResponse("Hello " + str(year))

class TestView(View):
    def get(self, request):
        return HttpResponse("TESTING")
    def post(self, request):
        pass