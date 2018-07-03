# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from login.models import User


class Question(models.Model):
    """
    Modelo pregunta
    """

    DIFICULTY_CHOISES = (
        ('E', "Easy"),
        ('N', 'Normal'),
        ('H', 'Hard'),
    )

    CATEGORY_CHOISES = (
        ('H', "History"),
        ('G', "Geography"),
        ('SC', "Science"),
        ('SP', "Sports"),
        ('A', "Art"),
        ('E', "Entertainment"),
    )

    question = models.CharField(null=False, max_length=100, blank=False)
    category = models.CharField(
        null=False, max_length=2, choices=CATEGORY_CHOISES, default='E')
    dificulty = models.CharField(
        null=False, max_length=1, choices=DIFICULTY_CHOISES, default='N')
    correctop = models.IntegerField(default=1)
    time = models.IntegerField(default=30)
    reward = models.IntegerField(default=100)
    cost = models.IntegerField(default=50)

    def __unicode__(self):
        return self.question


class Answer(models.Model):
    """
    Modelo Opcion
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, blank=False)
    is_correct = models.BooleanField(default=False)

    def __unicode__(self):
        return self.answer


class QuestionUser(models.Model):
    """
    Modelo QuestionUser
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
