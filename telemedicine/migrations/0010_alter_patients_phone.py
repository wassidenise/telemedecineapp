# Generated by Django 3.2.7 on 2021-09-28 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemedicine', '0009_alter_patients_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='phone',
            field=models.PositiveIntegerField(max_length=10, null=True),
        ),
    ]
