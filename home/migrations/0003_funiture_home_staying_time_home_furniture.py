# Generated by Django 4.1.5 on 2023-03-24 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funiture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='home',
            name='staying_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='furniture',
            field=models.ManyToManyField(to='home.funiture'),
        ),
    ]
