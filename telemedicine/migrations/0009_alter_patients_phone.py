# Generated by Django 3.2.7 on 2021-09-28 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemedicine', '0008_auto_20210928_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]
