# Generated by Django 4.1.5 on 2023-01-23 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_home_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='banner',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
