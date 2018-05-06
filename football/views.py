from datetime import datetime
from django.db.models.functions import Lower
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from football.models import Data, Summary, DataForm
from django.views.generic.edit import UpdateView


class HomeView(generic.ListView):
    template_name = 'football/home.html'
    context_object_name = 'summary'

    def get_queryset(self):
        return Summary.objects.all().order_by(Lower('total').desc())


def predict(request):
        template = loader.get_template('football/predict.html')
        try:
            datas = Data.objects.filter(user_data__username=request.user,schedule__match_date__gt=datetime.now())
            context = {
                'datas': datas,
            }
            return HttpResponse(template.render(context, request))
        except Data.DoesNotExist:
            return render(request, 'football/nodata.html')


class VoteView(UpdateView):
    form_class = DataForm
    model = Data
    template_name = 'football/vote.html'
    success_url = '/predict/'

    def get_object(self, queryset=None):
        obj = Data.objects.get(id=self.kwargs['data_id'],schedule__match_date__gt=datetime.now())
        return obj

def reference(request, data_id):
    data = get_object_or_404(Data, pk=data_id)
    userdatas=Data.objects.filter(schedule=data.schedule)
    template = loader.get_template('football/reference.html')
    context = {
        'userdatas': userdatas,
    }
    return HttpResponse(template.render(context, request))

class ResultView(generic.ListView):
    template_name = 'football/result.html'
    context_object_name = 'user_data'

    def get_queryset(self):
        return Data.objects.filter(user_data__username=self.request.user)

def rule(request):
    return render(request, 'football/rule.html')

def user(request):
    return render(request, 'football/user.html')