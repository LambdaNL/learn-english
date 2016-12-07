from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from .models import QuestionnaireTable
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


def results(request):
    unique_users = get_unique_usernames(Questionnaire.objects.all())
    table = QuestionnaireTable(Questionnaire.objects.all())

    return render_to_response("exercises/results.html", {"table": table},
                              context_instance=RequestContext(request))
