# Generated by Django 3.0.7 on 2020-06-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_uploadproperties_property_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadproperties',
            name='bedrooms',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='uploadproperties',
            name='commission',
            field=models.CharField(choices=[('10', '10'), ('20', '20'), ('30', '30'), ('40', '40'), ('50', '50'), ('60', '60'), ('70', '70'), ('80', '80')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='uploadproperties',
            name='garage',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='uploadproperties',
            name='toilet',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=10, null=True),
        ),
    ]
