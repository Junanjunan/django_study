# Generated by Django 4.1.5 on 2023-01-04 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruits',
            name='grade',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]