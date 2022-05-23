from django.db import models


class Rewards(models.Model):
    image = models.ImageField(
        verbose_name="Изображение"
    )


class Employee(models.Model):
    image = models.ImageField(
        verbose_name="Изображение"
    )
    name = models.CharField(
        max_length=120,
        verbose_name="Имя"
    )
    role = models.CharField(
        max_length=120,
        verbose_name="Должность"
    )
    salary = models.IntegerField(
        default=0,
        verbose_name="Зарплата"
    )
    description = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return f"{self.name} > {self.role}"


class Feedback(models.Model):
    author = models.CharField(
        max_length=100, verbose_name='Автор'
    )
    email = models.EmailField(
        max_length=100
    )
    subject = models.CharField(
        max_length=100, verbose_name='Предмет'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
