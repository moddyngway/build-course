# Generated by Django 4.0.4 on 2022-05-18 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100, verbose_name='Предмет')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
        ),
    ]
