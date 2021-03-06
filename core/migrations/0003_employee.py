# Generated by Django 4.0.4 on 2022-05-18 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_rewards_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('name', models.CharField(max_length=120, verbose_name='Имя')),
                ('role', models.CharField(max_length=120, verbose_name='Должность')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
