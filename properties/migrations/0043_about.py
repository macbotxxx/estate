# Generated by Django 3.0.7 on 2020-07-07 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0042_fqa'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(null=True)),
                ('company_image', models.ImageField(null=True, upload_to='about_image/')),
            ],
        ),
    ]
