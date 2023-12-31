# Generated by Django 4.2.2 on 2023-06-26 22:13

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import fullweb.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='appuser',
            managers=[
                ('object', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='appuser',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(6), fullweb.accounts.validators.letters_numbers_underscore_validator]),
        ),
    ]
