# Generated by Django 4.2.2 on 2023-06-29 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_appuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='date_joined',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 29, 19, 23, 35, 398407), null=True),
        ),
    ]
