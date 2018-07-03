"""quizfun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from login import views

# Direcciones url de QuizFun
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^in/$', login, {'template_name': 'login/login.html'}, name='login'),
    url(r'^home/in/$', login,
        {'template_name': 'login/login.html'}, name='login'),
    url(r'^logout/', logout, {'next_page': '/in'}, name='logout'),
    url(r'^login/home/logout/', logout, {'next_page': '/in'}, name='logout'),
    url(r'^accounts/login/$', login,
        {'template_name': 'login/login.html'}, name='login2'),
    url(r'^login', include('login.urls')),
    url(r'^admin/logout', views.signout, name='signout'),
    url(r'^admin/', admin.site.urls),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^home/profile/', views.profile, name='profile'),
    url(r'^change_password/', views.change_password, name='change_password'),
    url(r'^password/', views.change_password, name='change_password'),
    url(r'^password_changed/', views.password_changed, name='password_changed'),
    url(r'^login/register/login/registered/',
        views.registered, name='registered'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^preguntas/', include('preguntas.urls')),
    url(r'^ranking/', include('ranking.urls')),
    url(r'^predictions/', include('predictions.urls')),
    url(r'^questions/', include('preguntas.urls')),
    url(r'^clear/', views.changeflag, name='flag'),
]
# Codigo para manejar url de avatars
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
