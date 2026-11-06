from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    # Поле вывода количества уроков в курсе
    lessons_count = SerializerMethodField()

    def get_lessons_count(self, obj):
        return obj.lesson_set.count()

    # Поле вывода уроков
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('title', 'description', 'lessons_count', 'lessons')
