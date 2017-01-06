from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from . import models

from .score_calculator import *


def index(request):
    return render(request, 'exercises/index.html')


def exercise(request, level, name):
    if request.method != 'POST' and level != '':
        return render(request, 'exercises/' + name + '/' + level + '.html')
    elif request.method == 'POST':
        questionnaire_result = Questionnaire(
            level=level,
            username=request.POST['username'],
            question_1=request.POST['question_1'],
            question_2=request.POST['question_2'],
            question_3=request.POST['question_3'],
            question_4=request.POST['question_4'],
            question_5=request.POST['question_5'],
        )
        questionnaire_result.save()
        return HttpResponse("Answers submitted!")
    else:
        return render(request, 'exercises/' + name + '/' + name + '.html')


def adverbs(request, level):
    if request.method != 'POST' and level != '':
        return render_to_response('exercises/adverbs/' + level + '.html',
                                  {'open_questions': models.OpenQuestion.objects.filter(category=level)},
                                  context_instance=RequestContext(request))

    elif request.method == 'POST':
        for q in models.OpenQuestion.objects.filter(category=level):
            if request.POST[str(q.pk)] != '':
                foq = models.FilledOpenQuestion(
                    username=request.POST['username'],
                    question=q.question,
                    answer=request.POST[str(q.pk)])
                foq.save()
            else:
                render_to_response('exercises/adverbs/' + level + '.html',
                                   {'open_questions': models.OpenQuestion.objects.filter(category=level)},
                                   context_instance=RequestContext(request))

        return render_to_response('exercises/index.html', context_instance=RequestContext(request))
    else:
        return render(request, 'exercises/adverbs/adverbs.html')


def results(request):
    unique_users = get_unique_usernames(models.FilledOpenQuestion.objects.all())

    for user in unique_users:
        all_questions = models.FilledOpenQuestion.objects.filter(username=user)
        correct_amount = get_correct_amount(all_questions)
        incorrect_amount = get_incorrect_amount(all_questions)

        get
        new_user = models.UserScore.objects.create(username=user, totalCorrect=0, totalIncorrect=0)
        new_user.totalCorrect = correct_amount
        new_user.totalInCorrect = incorrect_amount
        new_user.save()

    return render_to_response("exercises/results.html", {"users": models.UserScore.objects.all()},
                              context_instance=RequestContext(request))


def find_correct_answer(question):
    return models.OpenQuestion.objects.get(question=question)
