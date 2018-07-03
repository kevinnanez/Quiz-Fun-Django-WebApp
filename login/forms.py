from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserProfile
from .models import *


# Formulario para registrarse
class UserProfileForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'hobbies',
            'favcategory',
            'picture',
        ]

    def save(self, commit=True):

        user = super(UserProfileForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.coins = 100
        if commit:
            user.save()
        return user


# Formulario para editar perfil
class EditProfileForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'age',
            'hobbies',
            'favcategory',
            'picture',
        )
