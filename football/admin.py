from django.contrib import admin
from .models import Schedule


# Register your models here.
class ScheduleAdmin(admin.ModelAdmin):
    fields = ['match_date','team_a', 'team_b', 'level','score_a', 'score_b','result_point','score_point']
    list_display = ('match_date','team_a', 'team_b', 'level', 'score_a', 'score_b','result_point','score_point')
    list_filter = ['match_date']


admin.site.register(Schedule, ScheduleAdmin)
