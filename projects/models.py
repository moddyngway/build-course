import datetime

from django.contrib.auth.models import User
from django.db import models
import random


class Category(models.Model):
    title = models.CharField(
        max_length=70,
        verbose_name='Название'
    )
    code = models.CharField(
        max_length=70
    )

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(
        max_length=70,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    categories = models.ManyToManyField(
        Category, verbose_name='Категории'
    )

    @property
    def category_codes(self):
        codes = []
        for category in self.categories.all():
            codes.append(f'filter-{category.code}')
        return ' '.join(codes)


    @property
    def images(self):
        print(ProjectImages.objects.filter(project_id=self.pk).order_by('pk'))
        return ProjectImages.objects.filter(project_id=self.pk).order_by('pk')


    @property
    def image(self):
        print(self.images.first().image.url)
        print(self.images.first())
        return self.images.first()

    def __str__(self):
        return self.title


class ProjectImages(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        verbose_name='Проект'
    )
    image = models.ImageField(
        verbose_name='Картинка'
    )


class Check(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        verbose_name='Проект'
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )
    client = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, verbose_name="Покупатель"
    )
    date = models.DateField(
        verbose_name='Дата', default=datetime.date(2022, 1, 1)
    )

    def create_random(self):
        projects_list = Project.objects.all()
        for i in range(300):
            bulk = []
            for j in range(1_000):
                bulk.append(Check(
                    project=random.choice(projects_list),
                    price=random.randint(800_000, 10_000_000),
                    client=User.objects.first(),
                    date=datetime.date(
                        year=random.randint(2016, 2022),
                        month=random.randint(1, 12),
                        day=random.randint(1, 25)
                    )
                ))
            Check.objects.bulk_create(bulk)
            print(i)

    def __str__(self):
        return f"{self.project.title} -> {self.price} -> {self.client}"
