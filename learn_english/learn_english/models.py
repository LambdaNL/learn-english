from django.db import models


class Question(models.Model):
    username = models.CharField(max_length=200)
    score = models.IntegerField(max_length=100)
