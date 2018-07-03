# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader

from random import randint

from django.http import JsonResponse

from django.contrib.auth.models import User
from login.models import UserProfile


@login_required
def rankingmenu(request):
    """
    Metodo que provee al usuario la opcion de elegir entre ranking mesual y global
    """
    template = loader.get_template('ranking/rankingmenu.html')
    user = request.user
    coins = user.userprofile.coins
    context = {
    }
    return HttpResponse(template.render(context, request))


@login_required
def rankingglobal(request):
    """
    Metodo que muestra al usuario el ranking global
    """
    template = loader.get_template('ranking/rankingglobal.html')
    user = request.user
    coins = user.userprofile.coins
    all_users = UserProfile.objects.all()
    all_users = all_users.order_by('-coins')
    context = {
        'all_users': all_users,
    }
    return HttpResponse(template.render(context, request))


@login_required
def rankingmensual(request):
    """
    Metodo que muestra al usuario el ranking mensual
    """
    template = loader.get_template('ranking/rankingmensual.html')
    user = request.user
    coins = user.userprofile.coins
    all_users = UserProfile.objects.all()
    all_users = all_users.order_by('-coins')
    context = {
        'all_users': all_users,
    }
    return HttpResponse(template.render(context, request))


@login_required
def userprofile(request, user_id):
    """
    Metodo que muestra al usuario el perfil de otro usuario desde el ranking mensual
    o global
    """
    template = loader.get_template('profile/userprofile.html')
    user = UserProfile.objects.get(pk=user_id)
    context = {
        'user': user
    }
    return HttpResponse(template.render(context, request))
