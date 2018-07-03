# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField
# Create your models here.


# Modelo de usuario
class UserProfile(User):
    # Categorias
    CATEGORY_CHOISES = (
        ('H', "History"),
        ('G', "Geography"),
        ('SC', "Science"),
        ('SP', "Sports"),
        ('A', "Art"),
        ('E', "Entertainment"),
    )
    # Campos de usuario extendiendo User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=30, null=True, blank=True)
    hobbies = models.CharField(max_length=30, null=True, blank=True)
    favcategory = MultiSelectField(choices=CATEGORY_CHOISES)
    picture = models.ImageField(blank=True)
    coins = models.IntegerField(default=100)
    daily = models.BooleanField(default=False)
    newquestions = models.BooleanField(default=False)


def __str__(self):
    return self.user.username


# Crea perfil. Para que ande el registro del SuperUser, comentar todo el
# bloque a partir de aqui
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
