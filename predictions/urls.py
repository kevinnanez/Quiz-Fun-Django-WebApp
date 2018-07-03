from django.conf.urls import url

from . import views
from .views import *
from django.views.generic import TemplateView

# We are adding a URL called /home
urlpatterns = [
    url(r'^list', views.predictionlist, name='predictionlist'),
    url(r'^prediction/', views.prediction, name='prediction'),
    url(r'^bet_prediction/', views.bet_prediction, name='bet_prediction'),
]
