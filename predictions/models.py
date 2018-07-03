# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from login.models import User

# Create your models here.
# Modelo de una Prediccion


class Prediction(models.Model):
    """
    Modelo prediccion
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

    prediction = models.CharField(null=False, max_length=100, blank=False)
    state = models.CharField(null=False, max_length=30, default="Incompleta",
                             blank=False)
    category = models.CharField(null=False, max_length=2,
                                choices=CATEGORY_CHOISES, default='E')
    dificulty = models.CharField(null=False, max_length=1,
                                 choices=DIFICULTY_CHOISES, default='N')
    reward = models.DecimalField(default=2.00, max_digits=9, decimal_places=2)
    start_time = models.DateTimeField(help_text="<em>yyyy-mm-dd hh:mm</em>.")
    end_time = models.DateTimeField(help_text="<em>yyyy-mm-dd hh:mm</em>.")

    def __unicode__(self):
        return self.prediction


class AnswerPred(models.Model):
    """
    Modelo Opcion de Prediccion
    """
    prediction = models.ForeignKey(Prediction, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __unicode__(self):
        return self.answer


class PredictionUser(models.Model):
    """
    Modelo Prediccion Respondida por Usuario
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prediction = models.ForeignKey(Prediction, on_delete=models.CASCADE)
    answer = models.ForeignKey(AnswerPred, on_delete=models.CASCADE)
    bet = models.IntegerField(blank=False)
    state = models.CharField(null=False, max_length=30, default="No updated",
                             blank=False)
