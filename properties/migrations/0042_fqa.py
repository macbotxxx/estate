# Generated by Django 3.0.7 on 2020-07-07 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0041_auto_20200706_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='FQA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400, null=True)),
                ('answer', models.CharField(max_length=400, null=True)),
            ],
        ),
    ]
