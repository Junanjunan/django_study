# Generated by Django 4.1.5 on 2023-01-06 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruits', '0003_fruits_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('fruits', models.ManyToManyField(to='fruits.fruits')),
            ],
        ),
    ]
