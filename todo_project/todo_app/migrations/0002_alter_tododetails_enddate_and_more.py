# Generated by Django 5.1.1 on 2024-09-24 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tododetails',
            name='enddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tododetails',
            name='startdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
