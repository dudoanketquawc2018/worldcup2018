# Generated by Django 2.0.1 on 2018-02-10 15:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=200)),
                ('predict_winner', models.CharField(choices=[('AWIN', 'Đội A'), ('BALANCE', 'Hòa'), ('BWIN', 'Đội B'), ('-', '-')], default='-', max_length=200)),
                ('predict_score', models.BooleanField(default=False)),
                ('predict_score_a', models.IntegerField(default=0)),
                ('predict_score_b', models.IntegerField(default=0)),
                ('reward', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_date', models.DateTimeField(default=datetime.datetime(2018, 2, 10, 22, 25, 16, 566937))),
                ('team_a', models.CharField(max_length=200)),
                ('team_b', models.CharField(max_length=200)),
                ('score_a', models.IntegerField(default=-1)),
                ('score_b', models.IntegerField(default=-1)),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.Schedule'),
        ),
        migrations.AddField(
            model_name='data',
            name='user_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]