# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader


from random import randint

from django.http import JsonResponse

from .models import Question, Answer, QuestionUser

from django.contrib.auth.models import User


# Create your views here.
@login_required
def nocoins(request):
    """
    Metodo que se encarga de manejar cuando el usuario no tiene las monedas suficientes para jugar
    """
    template = loader.get_template('questions/nocoins.html')
    user = request.user
    coins = user.userprofile.coins
    context = {
        'message': "You don't have the necessary amount of coins to" +
                   "play. It's required to have at least 10 coins, and you have " +
                   coins + ".",
    }
    return HttpResponse(template.render(context, request))


@login_required
def noquestions(request):
    """
    Metodo que se encarga de manejar cuando el sistemas ya no tiene preguntas para el usuario
    """
    template = loader.get_template('questions/home.html')
    context = {
        'message': "You have already answer all the available questions" +
                   " you won't be able to play for now",
    }
    return HttpResponse(template.render(context, request))


@login_required
def questiondetail(request):
    """
    Metodo que se encarga de mostrar el detalle de una pregunta aleatoria
    """
    mincoins = 10
    user = request.user
    userid = user.id
    excluded_question = (QuestionUser.objects.filter(user=userid).
                         values('question'))
    questions = Question.objects.exclude(id__in=excluded_question)
    length = len(questions)
    if(length == 0):
        template = loader.get_template('home.html')
        context = {
            'message': "You have already answer all the available questions" +
                       " you won't be able to play for now",
        }
        return HttpResponse(template.render(context, request))
    # print (str)(length)+"hola"
    random = randint(0, length - 1)

    question = questions[random]
    answers = Answer.objects.filter(question=question.id)

    if user.userprofile.coins >= mincoins:
        if(user.userprofile.coins > question.cost):
            user.userprofile.coins -= question.cost
        else:
            user.userprofile.coins = 0
        user.userprofile.save()
        template = loader.get_template('questions/ask_question.html')
        context = {
            'user': request.user,
            'question': question,
            'answers': answers,
        }
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('questions/nocoins.html')
        coins = user.userprofile.coins
        context = {
            'message': "You don't have the necessary amount of coins to " +
                       " play. It's required to have at least 10 coins, " +
                       " and you have" + (str)(coins) + ".",
        }
        return HttpResponse(template.render(context, request))


@login_required
def questionresult(request, question_id, option_choise):
    """
    Metodo que se encarga de validar la respuesta del usuario y chequear su correctidud
    """

    user = request.user
    question = get_object_or_404(Question, pk=question_id)

    if question.correctop == option_choise:
        template = loader.get_template('questions/correcta.html')
        context = {
            'user': request.user,
            'question': question,
        }
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('questions/incorrecta.html')
        context = {
            'user': request.user,
            'question': question,
        }
        return HttpResponse(template.render(context, request))


def answer_question(request):
    """
    Metodo que se encarga de chequear respuesta del usuario
    """
    question_id = request.GET.get('question', None)
    option = request.GET.get('option', None)
    user_id = request.GET.get('user', None)
    question = get_object_or_404(Question, pk=question_id)
    user = get_object_or_404(User, pk=user_id)
    answer = get_object_or_404(Answer, pk=option)

    if answer.is_correct:
        coins_temp = (int)(question.reward) + (int)(user.userprofile.coins)
        user.userprofile.coins = coins_temp
        qu = QuestionUser()
        qu.question = question
        qu.user = user
        qu.save()
        user.userprofile.save()
        data = {
            'is_correct': True
        }
    else:
        data = {
            'is_correct': False
        }
    return JsonResponse(data)
