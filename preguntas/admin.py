from django.contrib import admin
from models import Question, Answer
from django.forms.models import BaseInlineFormSet
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from django.contrib.admin import AdminSite
from login.models import UserProfile


class QuestionAnswerInline(admin.StackedInline):
    fields = ('question', 'answer', 'is_correct')
    model = Answer
    extra = 2
    min_num = 2

    class Media:
        js = ('quest_answer_radio.js',)


class QuestionAdmin(admin.ModelAdmin):
    fields = ('question', 'category', 'dificulty', 'time', 'reward', 'cost')
    inlines = [QuestionAnswerInline]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'creator', None) is None:
            obj.creator = request.user
        queryset = UserProfile.objects.all().update(newquestions=True)
        obj.save()


class MyAdminSite(AdminSite):
    site_url = 'http://127.0.0.1:8000/'


admin_site = MyAdminSite(name='myadmin')
admin.site.register(Question, QuestionAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
