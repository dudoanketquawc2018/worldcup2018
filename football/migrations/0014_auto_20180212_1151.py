# Generated by Django 2.0.1 on 2018-02-12 04:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0013_auto_20180212_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='match_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 12, 11, 51, 56, 999201)),
        ),
    ]
