# Generated by Django 3.0.7 on 2020-07-17 09:16

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0047_auto_20200716_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadproperties',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]