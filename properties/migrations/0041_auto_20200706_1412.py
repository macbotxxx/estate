# Generated by Django 3.0.7 on 2020-07-06 13:12

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0040_auto_20200706_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadproperties',
            name='description',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]
