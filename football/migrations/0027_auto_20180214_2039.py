# Generated by Django 2.0.1 on 2018-02-14 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0026_auto_20180214_0725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='match_point',
            new_name='result_point',
        ),
        migrations.AddField(
            model_name='schedule',
            name='level',
            field=models.CharField(choices=[('1-32', 'Vòng loại'), ('1-16', 'Vòng 1-16'), ('Quarterfinal', 'Tứ kết'), ('Semifinal', 'Bán kết'), ('Final', 'Chung kết')], default='1-32', max_length=200),
        ),
        migrations.AddField(
            model_name='schedule',
            name='score_point',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='match_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 14, 20, 38, 52, 923809)),
        ),
    ]