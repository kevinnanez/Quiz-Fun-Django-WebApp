from django.conf.urls import url

from . import views
from .views import *

# We are adding a URL called /home
urlpatterns = [
    url(r'^ranking_menu/$', views.rankingmenu, name='rankingmenu'),
    url(r'^ranking_mensual/$', views.rankingmensual, name='rankingmensual'),
    url(r'^ranking_global/$', views.rankingglobal, name='rankingglobal'),
    url(r'^userprofile/(?P<user_id>[0-9]+)$',
        views.userprofile, name='userprofile'),
]
