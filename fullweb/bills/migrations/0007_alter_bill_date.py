# Generated by Django 4.2.2 on 2023-07-05 21:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0006_alter_bill_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, max_length=20),
        ),
    ]