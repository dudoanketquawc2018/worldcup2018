# Generated by Django 2.0.1 on 2018-02-13 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0024_auto_20180213_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='match_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 13, 22, 22, 3, 270807)),
        ),
    ]