from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name='Название'
    )
    code = models.CharField(
        max_length=120,
        verbose_name='Код'
    )

    @property
    def count(self):
        return self.blog_set.count()

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name='Название'
    )
    image = models.ImageField(
        verbose_name='Картинка'
    )
    upload_date = models.DateField(
        auto_created=True
    )
    categories = models.ManyToManyField(
        Category, verbose_name="Категории"
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    text = models.TextField(
        verbose_name='Текст'
    )

    @property
    def category_list(self):
        return self.categories.all()

    def __str__(self):
        return self.title
