# Generated by Django 3.2.6 on 2021-08-31 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leocodersapp', '0002_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='date',
            field=models.DateField(default=datetime.date.today, help_text='YYYY-MM-DD', verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='patient_name',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='schedule',
            name='timeslot',
            field=models.IntegerField(choices=[(0, '09:00 – 19:00'), (1, '10:00 – 11:00'), (2, '11:00 – 12:00'), (3, '12:00 – 13:00'), (4, '13:00 – 14:00'), (5, '14:00 – 15:00'), (6, '15:00 – 16:00'), (7, '16:00 – 17:00'), (8, '17:00 – 18:00')], default=None),
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together={('user', 'date', 'timeslot')},
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='start_time',
        ),
    ]
