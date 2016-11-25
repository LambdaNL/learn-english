from django.db import models


class Adverb(models.Model):
    sentence = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    level = models.CharField(max_length=2)


class Answer(models.Model):
    username = models.CharField(max_length=20)
    question = models.CharField(max_length=200)
    correct = models.IntegerField()
    answered = models.IntegerField()
