# Generated by Django 3.2.5 on 2021-07-26 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=2000)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('participants', models.ManyToManyField(related_name='appointments', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='core.project')),
            ],
        ),
    ]
