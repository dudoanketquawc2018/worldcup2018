# Generated by Django 2.0.1 on 2018-02-12 04:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('football', '0012_auto_20180212_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winner_number', models.IntegerField(default=0)),
                ('winner_point', models.IntegerField(default=0)),
                ('score_number', models.IntegerField(default=0)),
                ('score_point', models.IntegerField(default=0)),
                ('total_reward', models.IntegerField(default=0)),
                ('user_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='score_result',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data',
            name='winner_result',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='match_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 12, 11, 43, 27, 946000)),
        ),
    ]