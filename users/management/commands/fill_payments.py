from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from materials.models import Course, Lesson
from users.models import Payment

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        user_1 = User.objects.filter(email='test_1@test.com').first()
        if not user_1:
            user_1 = User(email='test_1@test.com')
            user_1.set_password('123qwe')
            user_1.save()

        user_2 = User.objects.filter(email='test_2@test.com').first()
        if not user_2:
            user_2 = User(email='test_2@test.com')
            user_2.set_password('123qwe')
            user_2.save()

        course = Course.objects.first()
        lesson = Lesson.objects.first()

        Payment.objects.all().delete()

        p1 = Payment(
            user_id=user_1.id,
            paid_course_id=course.id,
            paid_lesson_id=None,
            amount=10000.00,
            payment_method=Payment.TRANSFER,
        )

        p2 = Payment(
            user_id=user_2.id,
            paid_course_id=None,
            paid_lesson_id=lesson.id,
            amount=2300.00,
            payment_method=Payment.CASH,
        )

        p1.save()
        p2.save()

        self.stdout.write(self.style.SUCCESS('Успешно добавлено 2 платежа'))
