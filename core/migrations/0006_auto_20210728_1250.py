# Generated by Django 3.2.5 on 2021-07-28 03:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210728_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='end_time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=1800)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(limit_choices_to={'is_staff': False}, on_delete=django.db.models.deletion.CASCADE, related_name='client_appointments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='employee',
            field=models.ManyToManyField(limit_choices_to={'is_staff': True}, related_name='employee_appointments', to=settings.AUTH_USER_MODEL),
        ),
    ]
