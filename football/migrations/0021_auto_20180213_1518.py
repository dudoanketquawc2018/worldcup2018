# Generated by Django 2.0.1 on 2018-02-13 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0020_auto_20180213_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='match_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 13, 15, 18, 50, 730216)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='score_a',
            field=models.CharField(choices=[('no', 'Chưa thi đấu'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], default='no', max_length=200),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='score_b',
            field=models.CharField(choices=[('no', 'Chưa thi đấu'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], default='no', max_length=200),
        ),
    ]
