from django.db import models
import django_tables2 as tables


class Questionnaire(models.Model):
    username = models.CharField(max_length=20)
    level = models.CharField(max_length=2)
    question_1 = models.CharField(max_length=100)
    question_2 = models.CharField(max_length=100)
    question_3 = models.CharField(max_length=100)
    question_4 = models.CharField(max_length=100)
    question_5 = models.CharField(max_length=100)


class QuestionnaireTable(tables.Table):
    class Meta:
        model = Questionnaire


class OpenQuestion(models.Model):
    category = models.CharField(max_length=2)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)


class FilledOpenQuestion(models.Model):
    username = models.CharField(max_length=20)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)


class MultipleChoice(models.Model):
    category = models.CharField(max_length=2)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)


class UserScore(models.Model):
    username = models.CharField(max_length=20)
    totalCorrect = models.IntegerField(default=0)
    totalIncorrect = models.IntegerField(default=0)
