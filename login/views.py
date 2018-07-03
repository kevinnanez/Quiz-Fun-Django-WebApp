# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.template import loader

from django.http import HttpResponse, HttpResponseRedirect
from .models import UserProfile
from django.http import JsonResponse
from login.management.commands.daily import dailycoins
import re
import random


from .forms import (
    UserProfileForm,
    EditProfileForm,
)


def index(request):
    return render(request, "index.html")


# view de registro
def registration(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # Si el formulario es valido
            profile = form.save(commit=False)
            # Si el usuario agrego una imagen, esta se guarda
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            # Guardar formulario
            form.save()
            # Una vez registrado, lo loguea
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login/registered')
        else:
            # si esta mal rellenado, se carga de nuevo registro
            return render(request, 'login/register.html', {'form': form})
    else:
        form = UserProfileForm()
        args = {'form': form}
        return render(request, 'login/register.html', args)


@login_required  # Requiere que este logueado
def edit_profile(request):
    if request.method == 'POST':
        # formulario enviado
        form = EditProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            profile = form.save(commit=False)
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            form.save()
            return redirect('/profile/profile')
    else:
        # formulario inicial
        form = EditProfileForm(instance=request.user.userprofile)

        args = {'form': form}
        return render(request, 'profile/edit_profile.html', args)


def dcoins(request):
    user = request.META.get('REMOTE USER', none)
    if user.coins < 10:
        message.success(request, 'You have new coins')
    dailycoins()


@login_required
def home(request):
    # si el usuario es admin lo lleva a la pagina de admins
    user = request.user
    if user.is_superuser:
        return HttpResponseRedirect("/admin")
    # si no, lo lleva a home
    else:
        qid = random.randint(1, 4)
        template = loader.get_template('home.html')
        context = {
            'qid': qid,
        }
        return HttpResponse(template.render(context, request))


def changeflag(request):
    user = request.user
    queryset = UserProfile.objects.filter(
        username__iexact=user).update(newquestions=False)
    user.userprofile.daily = False
    return render(request, "questions/clear.html")


@login_required
# Visualizar el profile
def profile(request, pk=None):
    storage = messages.get_messages(request)
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user, 'message': storage}
    return render(request, 'profile/profile.html', args)

# Pagina para cuando se cambia la contraseña correctamente


def password_changed(request):
    return render(request, "change_password/password_changed.html")

# Pagina para cuando se registra correctamente


def registered(request):
    return render(request, "login/registered.html")

# Cambiar contraseña


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your new password has been saved.')
            update_session_auth_hash(request, user)
            return redirect(reverse('index'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "change_password/change_password.html", {
        'form': form
    })


# Mensaje para decir si el usuario ya existe
def validate_username(request):
    username = request.GET.get('username', None)
    flag = User.objects.filter(username__iexact=username).exists()
    data = {
        'is_taken': flag
    }
    return JsonResponse(data)


# Mensaje para decir que las contraseñas no coinciden
def validate_pass(request):
    pass1 = request.GET.get('pass', None)
    match1 = re.search("^.*[a-zA-Z]+.*$", pass1)
    match2 = re.search("^.*[0-9]+.*$", pass1)
    data = {
        'es_valido': match1 != None and match2 != None
    }
    return JsonResponse(data)


def validate_password(request):
    pass1 = request.GET.get('password', None)
    username = request.GET.get('username', None)
    kwargs = {'username': username}
    user = User.objects.get(**kwargs)
    flag = user.check_password(pass1)
    data = {
        'match': flag
    }
    return JsonResponse(data)


def signout(request):
    logout(request)
    return render(request, "index.html")
