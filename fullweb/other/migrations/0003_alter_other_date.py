# Generated by Django 4.2.2 on 2023-07-01 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0002_alter_other_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='other',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 1, 7, 29, 40, 611284, tzinfo=datetime.timezone.utc), max_length=20),
        ),
    ]
