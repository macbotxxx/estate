# Generated by Django 3.0.7 on 2020-06-16 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0017_uploadproperties_payment_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadproperties',
            name='property_price',
            field=models.IntegerField(null=True),
        ),
    ]
