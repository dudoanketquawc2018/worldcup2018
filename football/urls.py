from django.conf.urls import url
from django.urls import path
from . import views

app_name = "football"
urlpatterns = [
    path('rule/', views.rule, name='rule'),
    path('predict/', views.predict, name='predict'),
    path('result/', views.ResultView.as_view(), name='result'),
    path('user/', views.user, name='user'),
    url(r'^(?P<data_id>[0-9]+)/vote/$', views.VoteView.as_view(), name='vote'),
    url(r'^(?P<data_id>[0-9]+)/reference/$', views.reference, name='reference'),
    url(r'^', views.HomeView.as_view(), name='home'),
]