# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.test import TestCase

from .models import Question, Answer


class QuestionTestCase(TestCase):

    def create_q(self):
        return Question.objects.create(question="Que es un perro?",
                                       category='E',
                                       dificulty='E',
                                       correctop=1,
                                       time=30,
                                       reward=100,
                                       cost=50)

    def create_a(self):
        q = self.create_q()
        return Answer.objects.create(question=q,
                                     answer="Un animal",
                                     is_correct=True)

    def create_q_bad(self):
        return Question.objects.create(question="Que es un perro?",
                                       category='E',
                                       dificulty='E',
                                       correctop=1,
                                       time=30,
                                       reward=100,
                                       cost=50)

    def test_q_creation(self):
        q = self.create_q()
        self.assertTrue(isinstance(q, Question))
        self.assertEqual(q.__unicode__(), q.question)

    def test_q_creation_bad(self):
        q = self.create_q()
        self.assertTrue(isinstance(q, Question))
        self.assertEqual(q.__unicode__(), q.question)

    def test_a_creation(self):
        a = self.create_a()
        q = self.create_q()
        self.assertTrue(isinstance(a, Answer))
        self.assertEqual(a.id, q.correctop)

    def test_url_dont_exists(self):
        resp = self.client.get('/pepito')
        self.assertEqual(resp.status_code, 404)

    def test_301(self):
        resp = self.client.get('/home')
        self.assertEqual(resp.status_code, 301)

    def test_302(self):
        resp = self.client.get('http://localhost:8000/questions/nocoins/')
        self.assertEqual(resp.status_code, 302)

    def test_200(self):
        resp = self.client.get('http://localhost:8000/')
        self.assertEqual(resp.status_code, 200)

    def test_404(self):
        q = self.create_q()
        url = "pepito123/"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
