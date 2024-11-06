from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets, permissions
from .models import Course, Category
from .serializers import CourseSerializer, CategorySerializer, LessonSerializer
from .paginators import CoursePagination
from rest_framework.decorators import action
from rest_framework.response import responses, Response


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active = True)
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = CoursePagination

    def get_queryset(self):
        query = self.queryset

        cate_id = self.request.query_params.get('category_id')
        if cate_id:
            query = query.filter(category_id = cate_id)

        q = self.request.query_params.get("q")
        if q:
            query = query.filter(subject__icontains=q)
        return query

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @action(methods=['get'], url_path='lessons', detail=True)
    def get_lessons(self, request, pk):
        lessons = self.get_object().lessons.filter(active=True)
        return Response(LessonSerializer(lessons, many=True, context={'request':request}).data)


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