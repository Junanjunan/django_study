# Generated by Django 4.1.5 on 2023-02-15 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruits', '0007_shopfake2'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=10)),
                ('b', models.CharField(max_length=10)),
                ('c', models.CharField(max_length=10)),
                ('d', models.CharField(max_length=10)),
            ],
        ),
    ]
