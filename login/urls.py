from django.conf.urls import url

from models import UserProfile
from . import views

app_name = 'login'
urlpatterns = [
    url(r'^/register/$', views.registration, name='registration'),
    url(r'^/home/$', views.home, name="home"),
    url(r'^/validate_username/$', views.validate_username,
        name="validate_username"),
    url(r'^/validate_password/$', views.validate_password,
        name="validate_password"),
]
