# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from datetime import *

from django.utils import timezone

from django.http import JsonResponse

from .models import Prediction, AnswerPred, PredictionUser

from django.contrib.auth.models import User


# Create your views here.


def predictionlist(request):

    cate = request.GET.get('cat', None)
    user = request.user
    all_answered = PredictionUser.objects.filter(user__username__iexact=user)
    prediction = Prediction.prediction
    if cate:
        all_predictions = Prediction.objects.filter(
            start_time__lte=timezone.now(), end_time__gte=timezone.now(), category=cate)
    else:
        all_predictions = Prediction.objects.filter(
            start_time__lte=timezone.now(), end_time__gte=timezone.now())
    length = len(all_predictions)
    if(length == 0):
        template = loader.get_template('predictions/list.html')
        context = {
            'message': "There are not available predictions" +
                       " in this category",
        }
    else:
        pred = get_object_or_404(Prediction, pk=1)
        template = loader.get_template('predictions/list.html')
        context = {
            'user': request.user,
            'all_predictions': all_predictions,
            'pred': pred,
            'all_answered': all_answered
        }
    return HttpResponse(template.render(context, request))


@login_required
def prediction(request):
    prediction_id = request.GET.get('id', None)
    prediction = get_object_or_404(Prediction, pk=prediction_id)
    options = AnswerPred.objects.filter(prediction=prediction.id)

    template = loader.get_template('predictions/prediction.html')
    context = {
        'user': request.user,
        'prediction': prediction,
        'answers': options,
    }
    return HttpResponse(template.render(context, request))


def bet_prediction(request):
    prediction_id = request.GET.get('prediction', None)
    option = request.GET.get('option', None)
    user_id = request.GET.get('user', None)
    bet = request.GET.get('bet', None)

    prediction = get_object_or_404(Prediction, pk=prediction_id)
    user = get_object_or_404(User, pk=user_id)
    answer = get_object_or_404(AnswerPred, pk=option)

    pu = PredictionUser()
    pu.prediction = prediction
    pu.user = user
    pu.answer = answer
    pu.bet = bet

    pu.save()
    user.userprofile.coins = user.userprofile.coins - (int)(bet)
    user.userprofile.save()
    data = {
        'ok': True
    }
    return JsonResponse(data)
