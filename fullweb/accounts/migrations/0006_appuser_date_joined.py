# Generated by Django 4.2.2 on 2023-06-29 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_appuser_date_joined_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]