# Generated by Django 3.2.6 on 2021-08-31 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leocodersapp', '0005_alter_schedule_timeslot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='timeslot',
            field=models.IntegerField(choices=[(0, '09:00 – 10:00'), (1, '10:00 – 11:00'), (2, '11:00 – 12:00'), (3, '12:00 – 13:00'), (4, '13:00 – 14:00'), (5, '14:00 – 15:00'), (6, '15:00 – 16:00'), (7, '16:00 – 17:00'), (8, '17:00 – 18:00')], default=None),
        ),
    ]
