# Generated by Django 4.2.2 on 2023-07-01 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='date',
            field=models.DateField(default=datetime.date(2023, 7, 1), max_length=20),
        ),
    ]
