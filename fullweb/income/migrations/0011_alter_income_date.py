# Generated by Django 4.2.2 on 2023-07-01 07:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0010_alter_income_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 1, 7, 31, 30, 727839, tzinfo=datetime.timezone.utc), max_length=20),
        ),
    ]