# Generated by Django 2.0.1 on 2018-02-11 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0008_auto_20180211_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='match_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 11, 17, 19, 6, 860407)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='match_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 11, 17, 19, 6, 860407)),
        ),
    ]
