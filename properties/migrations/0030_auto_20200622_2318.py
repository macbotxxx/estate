# Generated by Django 3.0.7 on 2020-06-22 22:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('properties', '0029_manage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Manage',
            new_name='Manager',
        ),
    ]
