from django.forms.widgets import HiddenInput
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.forms import ModelForm


class Schedule(models.Model):
    level1="1-32"
    level2="1-16"
    level3="Quarterfinal"
    level4="Semifinal"
    level5="Third place"
    level6="Final"
    level_choises = (
        (level1, 'Vòng bảng'),
        (level2, 'Vòng 1-16'),
        (level3, 'Tứ kết'),
        (level4, 'Bán kết'),
        (level5, 'Giải ba'),
        (level6, 'Chung kết')
    )
    none = -1
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    eleven = 11
    twelfth = 12
    thirteen = 13
    fourteen = 14
    fifteen = 15
    sixteen = 16
    seventeen = 17
    eighteen = 18
    nineteen = 19
    twenty = 20
    Score_choises = (
        (none, 'Chưa thi đấu'),
        (zero, '0'),
        (one, '1'),
        (two, '2'),
        (three, '3'),
        (four, '4'),
        (five, '5'),
        (six, '6'),
        (seven, '7'),
        (eight, '8'),
        (nine, '9'),
        (ten, '10'),
        (eleven, '11'),
        (twelfth, '12'),
        (thirteen, '13'),
        (fourteen, '14'),
        (fifteen, '15'),
        (sixteen, '16'),
        (seventeen, '17'),
        (eighteen, '18'),
        (nineteen, '19'),
        (twenty, '20')
    )
    match_date = models.DateTimeField(default=datetime.now())
    team_a = models.CharField(max_length=200)
    team_b = models.CharField(max_length=200)
    level = models.CharField(max_length=200, choices=level_choises, default=level1)
    score_a = models.IntegerField(choices=Score_choises, default=none)
    score_b = models.IntegerField(choices=Score_choises, default=none)
    result_point = models.IntegerField(default=1)
    score_point = models.IntegerField(default=5)


class Data(models.Model):
    AWIN = 'AWIN'
    BALANCE = 'BALANCE'
    BWIN = 'BWIN'
    NEW = '-'
    RESULT_CHOICES = (
        (AWIN, 'Đội A thắng'),
        (BALANCE, 'Hai đội hòa'),
        (BWIN, 'Đội B thắng'),
        (NEW, '-')
    )
    none = -1
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    eleven = 11
    twelfth = 12
    thirteen = 13
    fourteen = 14
    fifteen = 15
    sixteen = 16
    seventeen = 17
    eighteen = 18
    nineteen = 19
    twenty = 20
    Score_choises = (
        (none, 'Không chọn'),
        (zero, '0'),
        (one, '1'),
        (two, '2'),
        (three, '3'),
        (four, '4'),
        (five, '5'),
        (six, '6'),
        (seven, '7'),
        (eight, '8'),
        (nine, '9'),
        (ten, '10'),
        (eleven, '11'),
        (twelfth, '12'),
        (thirteen, '13'),
        (fourteen, '14'),
        (fifteen, '15'),
        (sixteen, '16'),
        (seventeen, '17'),
        (eighteen, '18'),
        (nineteen, '19'),
        (twenty, '20')
    )
    user_data = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    predict_winner = models.CharField(max_length=200, choices=RESULT_CHOICES, default=NEW)
    winner_result = models.BooleanField(default=False)
    predict_score_a = models.IntegerField(choices=Score_choises, default=none)
    predict_score_b = models.IntegerField(choices=Score_choises, default=none)
    score_result = models.BooleanField(default=False)
    reward = models.IntegerField(default=0)


class Summary(models.Model):
    user_data = models.ForeignKey(User, on_delete=models.CASCADE)
    winner_number = models.IntegerField(default=0)
    winner_point = models.IntegerField(default=0)
    score_number = models.IntegerField(default=0)
    score_point = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    total_reward = models.IntegerField(default=0)


class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = [ 'user_data', 'schedule', 'predict_winner', 'predict_score_a', 'predict_score_b']
        widgets = {
            'user_data': HiddenInput(),
            'schedule': HiddenInput(),
        }