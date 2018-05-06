from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from football.models import Data, Schedule, Summary


@receiver(post_save, sender=User)
@receiver(post_save, sender=Schedule)
def model_post_save(sender, **kwargs):
    alluser = User.objects.all()
    allschedule = Schedule.objects.all()
    for user in alluser:
        for scheduleset in allschedule:
            try:
                data = Data.objects.get(user_data=user, schedule=scheduleset)
                data.save()
            except Data.DoesNotExist:
                data = Data.objects.create(user_data=user, schedule=scheduleset)
                if scheduleset.score_a > -1:
                    if scheduleset.score_b > -1:
                        data.reward = - scheduleset.result_point
                    else:
                        data.reward = 0
                else:
                    data.reward = 0
                data.save()

    for user in alluser:
        for scheduleset in allschedule:
            data = Data.objects.get(user_data=user, schedule=scheduleset)
            if data.schedule.score_a > -1:
                if data.schedule.score_b > -1:
                    if data.schedule.score_a > data.schedule.score_b:
                        if data.predict_winner == 'AWIN':
                            data.winner_result = True
                            if data.predict_score_a > -1:
                                if data.predict_score_b > -1:
                                    if data.schedule.score_a == data.predict_score_a:
                                        if data.schedule.score_b == data.predict_score_b:
                                            data.score_result = True
                                        else:
                                            data.score_result = False
                                    else:
                                        data.score_result = False
                                else:
                                    data.score_result = False
                            else:
                                data.score_result = False
                        else:
                            data.winner_result = False
                            if data.predict_score_a > -1:
                                if data.predict_score_b > -1:
                                    if data.schedule.score_a == data.predict_score_a:
                                        if data.schedule.score_b == data.predict_score_b:
                                            data.score_result = True
                                        else:
                                            data.score_result = False
                                    else:
                                        data.score_result = False
                                else:
                                    data.score_result = False
                            else:
                                data.score_result = False
                    if data.schedule.score_a == data.schedule.score_b:
                        if data.predict_winner == 'BALANCE':
                            data.winner_result = True
                            if data.predict_score_a > -1:
                                if data.predict_score_b > -1:
                                    if data.schedule.score_a == data.predict_score_a:
                                        if data.schedule.score_b == data.predict_score_b:
                                            data.score_result = True
                                        else:
                                            data.score_result = False
                                    else:
                                        data.score_result = False
                                else:
                                    data.score_result = False
                            else:
                                data.score_result = False
                        else:
                            data.winner_result = False
                            if data.predict_score_a > -1:
                                if data.predict_score_b > -1:
                                    if data.schedule.score_a == data.predict_score_a:
                                        if data.schedule.score_b == data.predict_score_b:
                                            data.score_result = True
                                        else:
                                            data.score_result = False
                                    else:
                                        data.score_result = False
                                else:
                                    data.score_result = False
                            else:
                                data.score_result = False
                    if data.schedule.score_a < data.schedule.score_b:
                        if data.predict_winner == 'BWIN':
                            data.winner_result = True
                            if data.predict_score_a > -1:
                                if data.predict_score_b > -1:
                                    if data.schedule.score_a == data.predict_score_a:
                                        if data.schedule.score_b == data.predict_score_b:
                                            data.score_result = True
                                        else:
                                            data.score_result = False
                                    else:
                                        data.score_result = False
                                else:
                                    data.score_result = False
                            else:
                                data.score_result = False
                        else:
                            data.winner_result = False
                            if data.predict_score_a > -1:
                                if data.predict_score_b > -1:
                                    if data.schedule.score_a == data.predict_score_a:
                                        if data.schedule.score_b == data.predict_score_b:
                                            data.score_result = True
                                        else:
                                            data.score_result = False
                                    else:
                                        data.score_result = False
                                else:
                                    data.score_result = False
                            else:
                                data.score_result = False
            data.save()

    for user in alluser:
        for scheduleset in allschedule:
            data = Data.objects.get(user_data=user, schedule=scheduleset)
            if data.schedule.score_a > -1:
                if data.schedule.score_b > -1:
                    if data.winner_result:
                        if data.predict_score_a > -1:
                            if data.predict_score_b > -1:
                                if data.score_result:
                                    win = Data.objects.filter(schedule=scheduleset, predict_score_a__gt=-1,predict_score_b__gt=-1, score_result=True)
                                    failure = Data.objects.filter(schedule=scheduleset, predict_score_a__gt=-1,predict_score_b__gt=-1, score_result=False)
                                    data.reward = (data.schedule.score_point * failure.count()) / win.count()
                                else:
                                    data.reward = - data.schedule.score_point
                            else:
                                data.reward = 0
                        else:
                            data.reward = 0
                    else:
                        data.reward = - data.schedule.result_point
                        if data.predict_score_a > -1:
                            if data.predict_score_b > -1:
                                if data.score_result:
                                    win = Data.objects.filter(schedule=scheduleset, predict_score_a__gt=-1, predict_score_b__gt=-1, score_result=True)
                                    failure = Data.objects.filter(schedule=scheduleset, predict_score_a__gt=-1,predict_score_b__gt=-1, score_result=False)
                                    data.reward = (data.schedule.score_point * failure.count()) / win.count() - scheduleset.result_point
                                else:
                                    data.reward = - data.schedule.score_point - data.schedule.result_point
                            else:
                                data.reward = - data.schedule.result_point
                        else:
                            data.reward = - data.schedule.result_point
                else:
                    data.reward = 0
            else:
                data.reward = 0
            data.save()

    Summary.objects.all().delete()
    for user in alluser:
        datas = Data.objects.filter(user_data=user)
        summary = Summary.objects.create(user_data=user)
        for data in datas:
            if data.schedule.score_a > -1:
                if data.schedule.score_b > -1:
                    if data.winner_result:
                        summary.winner_number = summary.winner_number + 1
                        if data.predict_score_a > -1:
                            if data.predict_score_b > -1:
                                if data.score_result:
                                    summary.score_number = summary.score_number + 1
                                    summary.score_point = summary.score_point + data.reward
                                else:
                                    summary.score_point = summary.score_point + data.reward
                    else:
                        summary.winner_point = summary.winner_point - data.schedule.result_point
                        if data.predict_score_a > -1:
                            if data.predict_score_b > -1:
                                if data.score_result:
                                    summary.score_number = summary.score_number + 1
                                    summary.score_point = summary.score_point + data.reward + data.schedule.result_point
                                else:
                                    summary.score_point = summary.score_point + data.reward + data.schedule.result_point
        summary.total = summary.winner_number + summary.score_number
        summary.total_reward = summary.winner_point + summary.score_point
        summary.save()