# Generated by Django 3.2.6 on 2021-08-31 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leocodersapp', '0007_auto_20210831_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
