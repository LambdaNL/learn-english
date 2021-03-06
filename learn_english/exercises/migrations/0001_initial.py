# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-06 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilledOpenQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MultipleChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=2)),
                ('option_1', models.CharField(max_length=100)),
                ('option_2', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OpenQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=2)),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('level', models.CharField(max_length=2)),
                ('question_1', models.CharField(max_length=100)),
                ('question_2', models.CharField(max_length=100)),
                ('question_3', models.CharField(max_length=100)),
                ('question_4', models.CharField(max_length=100)),
                ('question_5', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserScore',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('totalCorrect', models.IntegerField(default=0)),
                ('totalIncorrect', models.IntegerField(default=0)),
                ('score', models.FloatField(default=0)),
            ],
        ),
    ]
