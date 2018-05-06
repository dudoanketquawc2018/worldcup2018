# Generated by Django 2.0.1 on 2018-02-13 07:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0017_auto_20180213_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='predict_score',
        ),
        migrations.AlterField(
            model_name='data',
            name='predict_score_a',
            field=models.CharField(choices=[(-1, 'Không chọn'), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')], default=-1, max_length=200),
        ),
        migrations.AlterField(
            model_name='data',
            name='predict_score_b',
            field=models.CharField(choices=[(-1, 'Không chọn'), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')], default=-1, max_length=200),
        ),
        migrations.AlterField(
            model_name='data',
            name='predict_winner',
            field=models.CharField(choices=[('AWIN', 'Đội A'), ('BALANCE', 'Hòa'), ('BWIN', 'Đội B'), ('-', '-')], default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='match_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 13, 14, 55, 52, 204408)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='score_a',
            field=models.CharField(choices=[(-1, 'Không chọn'), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')], default=-1, max_length=200),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='score_b',
            field=models.CharField(choices=[(-1, 'Không chọn'), (0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')], default=-1, max_length=200),
        ),
    ]
