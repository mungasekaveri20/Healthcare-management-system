# Generated by Django 3.0.5 on 2020-04-27 02:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.datetime(2020, 4, 27, 2, 50, 20, 921476, tzinfo=utc))),
                ('end_date', models.DateField(default=datetime.datetime(2020, 4, 27, 2, 50, 20, 921476, tzinfo=utc))),
                ('health_service_income', models.PositiveIntegerField(default=0)),
                ('patients_seen', models.SmallIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
