# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.test import TestCase

from .models import UserProfile
from .forms import UserProfileForm


class UserTestCase(TestCase):

    def create_user(self):
        u = User.objects.create(username="pepe21",
                                email="pepaso@gmail.com")
        #password1 = "pp212121",
        # password2 = "pp212121")

        return UserProfile.objects.create(user=u,
                                          age=21,
                                          hobbies="pc",
                                          favcategory='H',
                                          coins=100)

    def test_user_creation(self):
        u = self.create_user()
        self.assertTrue(isinstance(u, UserProfile))
        self.assertEqual(u.__unicode__(), u.username)

    def test_valid_form(self):
        w = UserProfile.objects.create(
            username='pepe22', email='pepaso@gmail.com', password1='pp222222', password2='pp222222')
        data = {'username': w.username, 'email': w.email,
                'password1': w.password1, 'password2': w.password2}
        form = UserProfileForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = Whatever.objects.create(title='Foo', body='')
        data = {'title': w.title, 'body': w.body, }
        form = WhateverForm(data=data)
        self.assertFalse(form.is_valid())
