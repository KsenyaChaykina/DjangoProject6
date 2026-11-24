from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Subscription
from materials.validators import validate_only_youtube_links


class LessonSerializer(ModelSerializer):
    link_to_video = [validate_only_youtube_links]

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

    # Поле признака подписки
    is_subscribed = SerializerMethodField()

    def get_is_subscribed(self, instance):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Subscription.objects.filter(
                user=request.user,
                course=instance
            ).exists()
        return False

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'lessons_count', 'lessons', 'owner', 'is_subscribed')
