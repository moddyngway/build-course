# Generated by Django 4.0.4 on 2022-05-22 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='date',
            field=models.DateField(default=datetime.date(2022, 1, 1), verbose_name='Дата'),
        ),
    ]
