# Generated by Django 2.0.1 on 2018-02-16 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0033_auto_20180216_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='match_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 16, 20, 23, 35, 454600)),
        ),
    ]