# Generated by Django 2.0.6 on 2018-10-20 11:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('UserDetails', '0012_auto_20181020_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dob',
            field=models.DateField(default=datetime.datetime(2018, 10, 20, 11, 7, 18, 406825, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='afternoon',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='evening',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='morning',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='night',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='prognosis',
            name='startTime',
            field=models.DateField(default=datetime.datetime(2018, 10, 20, 11, 7, 18, 408937, tzinfo=utc)),
        ),
    ]
