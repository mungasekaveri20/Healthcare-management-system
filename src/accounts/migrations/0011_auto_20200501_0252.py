# Generated by Django 3.0.5 on 2020-05-01 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0010_auto_20200501_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor',
            field=models.OneToOneField(limit_choices_to={'groups': 1}, on_delete=django.db.models.deletion.CASCADE, related_name='Doctor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='nurse',
            field=models.OneToOneField(limit_choices_to={'groups': 2}, on_delete=django.db.models.deletion.CASCADE, related_name='Nurse', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient',
            field=models.OneToOneField(limit_choices_to={'groups': 3}, on_delete=django.db.models.deletion.CASCADE, related_name='Patient', to=settings.AUTH_USER_MODEL),
        ),
    ]
