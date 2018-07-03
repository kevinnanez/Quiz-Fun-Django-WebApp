# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from login.models import User
from django.test import TestCase
from django.test import client
# Create your tests here.


class QuestionTestCase(TestCase):

    def test_url_dont_exists(self):
        resp = self.client.get('/pepito')
        self.assertEqual(resp.status_code, 404)

    def test_301(self):
        resp = self.client.get('/home')
        self.assertEqual(resp.status_code, 301)

    def test_200(self):
        #User.objects.create_user(username="pepe22", password="pp22222222")
        #self.c = client.Client()
        #self.c.login(username="pepe22", password="pp22222222")
        resp = self.client.get('accounts/login/?next=/ranking/ranking_global/')
        self.assertEqual(resp.status_code, 200)

    def test_404(self):
        url = "pepito123/"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
