# Generated by Django 3.0.5 on 2020-04-28 02:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20200428_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 28, 2, 49, 4, 57880, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='report',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 28, 2, 49, 4, 57858, tzinfo=utc)),
        ),
    ]
