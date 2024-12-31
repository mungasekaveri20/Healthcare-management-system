# Generated by Django 3.0.5 on 2020-04-27 03:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 27, 3, 1, 53, 593456, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='report',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 27, 3, 1, 53, 593456, tzinfo=utc)),
        ),
    ]