# Generated by Django 4.1.5 on 2023-01-23 01:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_home_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='banner',
            field=models.ImageField(null=True, upload_to=datetime.datetime(2023, 1, 23, 1, 29, 1, 35289)),
        ),
    ]
