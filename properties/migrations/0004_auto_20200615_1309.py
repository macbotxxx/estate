# Generated by Django 3.0.7 on 2020-06-15 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20200615_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadproperties',
            name='date_built',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
