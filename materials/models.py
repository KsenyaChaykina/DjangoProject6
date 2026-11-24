from django.conf import settings
from django.db import models


class Course(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название курса',
        help_text='Введите название курса',
    )
    image = models.ImageField(
        upload_to='materials/image',
        blank=True,
        null=True,
        verbose_name='Картинка',
        help_text='Загрузите картинку',
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание курса',
        help_text='Введите описание курса',
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Владелец',
        help_text='Укажите владельца курса',
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название урока',
        help_text='Введите название урока',
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name='Курс',
        help_text='Введите название курса',
        blank=True,
        null=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание урока',
        help_text='Введите описание урока',
    )
    image = models.ImageField(
        upload_to='materials/image',
        verbose_name='Картинка',
        blank=True,
        null=True
    )
    link_to_video = models.URLField(
        verbose_name='Ссылка на видео',
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Владелец',
        help_text='Укажите владельца урока',
    )

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


    def __str__(self):
        return self.title

class Subscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс',
        help_text='Укажите курс',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        # Что бы пользователь не подписался на один и тот же курс дважды
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'course'],
                name='unique_user_course_subscription',
            )
        ]

    def __str__(self):
        return f'{self.user} - {self.course}'
