# Generated by Django 2.2.1 on 2020-05-28 16:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management_portal', '0003_auto_20200528_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='developers',
        ),
        migrations.AddField(
            model_name='project',
            name='assigned_to',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
