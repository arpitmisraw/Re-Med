# Generated by Django 2.1.1 on 2018-10-19 19:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('UserDetails', '0006_auto_20181020_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dob',
            field=models.DateField(default=datetime.datetime(2018, 10, 19, 19, 11, 52, 952607, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prognosis',
            name='endTime',
            field=models.DateField(default=datetime.datetime(2018, 10, 19, 19, 11, 52, 968225, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prognosis',
            name='startTime',
            field=models.DateField(default=datetime.datetime(2018, 10, 19, 19, 11, 52, 968225, tzinfo=utc)),
        ),
    ]
