# Generated by Django 2.0.1 on 2018-02-14 00:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0025_auto_20180213_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='match_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 14, 7, 25, 56, 212401)),
        ),
    ]