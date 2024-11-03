from rest_framework.serializers import ModelSerializer
from .models import Course, Category


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'image', 'created_date', 'category']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']