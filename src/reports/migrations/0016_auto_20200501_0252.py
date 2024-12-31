# Generated by Django 3.0.5 on 2020-05-01 02:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0015_auto_20200501_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 1, 2, 52, 13, 220295, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='report',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 1, 2, 52, 13, 220276, tzinfo=utc)),
        ),
    ]
