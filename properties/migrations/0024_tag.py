# Generated by Django 3.0.7 on 2020-06-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0023_auto_20200617_0231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(choices=[('featured', 'featured'), ('popular', 'popular')], max_length=300, null=True)),
            ],
        ),
    ]
