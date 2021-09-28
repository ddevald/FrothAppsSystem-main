# Generated by Django 3.2.5 on 2021-08-02 02:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210728_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='duration',
            field=models.DurationField(choices=[('00:30:00', '30 minutes'), ('01:00:00', '1 hour'), ('01:30:00', '1.5 hour'), ('02:00:00', '2 hour')], default='00:30:00'),
        ),
    ]
