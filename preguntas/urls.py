from django.conf.urls import url

from . import views
from .views import *

# We are adding a URL called /home
urlpatterns = [
    url(r'^nocoins/$', views.nocoins, name='nocoins'),
    url(r'^noquestions/$', views.noquestions, name='noquestions'),
    url(r'^ask_question/$', views.questiondetail, name='questiondetail'),
    url(r'^(?P<question_id>[0-9]+)?option=(?P<option_choise>[0-9]+)$',
        views.questionresult, name='questionresult'),
    url(r'^answer_question/$', views.answer_question, name="answer_question"),
]
