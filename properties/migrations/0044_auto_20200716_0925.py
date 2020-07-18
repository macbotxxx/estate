# Generated by Django 3.0.7 on 2020-07-16 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0043_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amentities',
            name='amentity',
            field=models.CharField(max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='fqa',
            name='answer',
            field=models.CharField(max_length=400, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='fqa',
            name='question',
            field=models.CharField(max_length=400, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='partners',
            name='partner_name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='uploadproperties',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='uploadproperties',
            name='property_title',
            field=models.CharField(max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='workers',
            name='staff_phoneNumber',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
