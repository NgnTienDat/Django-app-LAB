from tkinter import image_names

from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import Course, Category, Lesson

class BaseSerializer(ModelSerializer):
    image = SerializerMethodField(source='image')

    def get_image(self, course):
        request = self.context.get('request')
        if request and course.image:
            return request.build_absolute_uri('/static/%s' % course.image)


class CourseSerializer(BaseSerializer):

    class Meta:
        model = Course
        fields = ['id', 'subject', 'image', 'created_date', 'category_id']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class LessonSerializer(BaseSerializer):

    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image', 'course_id']