# Generated by Django 2.0.7 on 2018-07-18 00:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userboard', '0004_auto_20180713_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='extra_additional_hour_percent',
        ),
        migrations.AddField(
            model_name='workhour',
            name='pause_duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AddField(
            model_name='workhour',
            name='public_holiday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workhour',
            name='salary_earned',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]