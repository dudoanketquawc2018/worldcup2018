# Generated by Django 2.0.1 on 2018-02-16 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0037_auto_20180216_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='match_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 16, 21, 37, 11, 792220)),
        ),
    ]
