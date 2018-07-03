# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Prediction, AnswerPred
from django.forms.models import BaseInlineFormSet
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from django.contrib.admin import AdminSite
from datetime import datetime

from django.utils import timezone


# Register your models here.

class PredictionAnswerInline(admin.StackedInline):
    fields = ('prediction', 'answer')
    model = AnswerPred
    extra = 2
    min_num = 2


class PredictionAnswerInline2(admin.StackedInline):
    fields = ('is_correct',)
    model = AnswerPred
    extra = 0
    max_num = 0

    class Media:
        js = ('pred_answer_radio.js',)


class PredictionAdmin(admin.ModelAdmin):
    fields = ('prediction', 'category', 'dificulty',
              'reward', 'start_time', 'end_time')
    inlines = [PredictionAnswerInline]
    other_inlines = [PredictionAnswerInline2]

    def get_inline_instances(self, request, obj=None):
        if(obj == None):
            self.inlines = [PredictionAnswerInline]
        else:
            if obj.end_time > timezone.now():
                self.inlines = [PredictionAnswerInline]
            else:
                self.inlines = [PredictionAnswerInline2]
        return super(PredictionAdmin, self).get_inline_instances(request, obj)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'creator', None) is None:
            obj.creator = request.user
        obj.save()


class MyAdminSite(AdminSite):
    site_url = 'http://127.0.0.1:8000/'


admin_site = MyAdminSite(name='myadmin')
admin.site.register(Prediction, PredictionAdmin)
