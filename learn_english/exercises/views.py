from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from .models import QuestionnaireTable
from .score_calculator import *


def index(request):
    return render(request, 'exercises/index.html')


def adverbs(request, level):
    if level == "A1":
        if request.method == 'POST':
            a1 = Questionnaire(
                level='A1',
                username=request.POST['username'],
                question_1=request.POST['question_1'],
                question_2=request.POST['question_2'],
                question_3=request.POST['question_3'],
                question_4=request.POST['question_4'],
                question_5=request.POST['question_5'],
            )
            a1.save()
            return HttpResponse("Answers submitted!")
        else:
            return render(request, 'exercises/adverbs/A1.html')
    elif level == "A2":
        if request.method == 'POST':
            a2 = Questionnaire(
                level='A2',
                username=request.POST['username'],
                question_1=request.POST['question_1'],
                question_2=request.POST['question_2'],
                question_3=request.POST['question_3'],
                question_4=request.POST['question_4'],
                question_5=request.POST['question_5'],
            )
            a2.save()
            return HttpResponse("Answers submitted!")
        else:
            return render(request, 'exercises/adverbs/A2.html')
    elif level == "B1":
        if request.method == 'POST':
            b1 = Questionnaire(
                level='B1',
                username=request.POST['username'],
                question_1=request.POST['question_1'],
                question_2=request.POST['question_2'],
                question_3=request.POST['question_3'],
                question_4=request.POST['question_4'],
                question_5=request.POST['question_5'],
            )
            b1.save()
            return HttpResponse("Answers submitted!")
        else:
            return render(request, 'exercises/adverbs/B1.html')
    elif level == "B2":
        if request.method == 'POST':
            b2 = Questionnaire(
                level='B2',
                username=request.POST['username'],
                question_1=request.POST['question_1'],
                question_2=request.POST['question_2'],
                question_3=request.POST['question_3'],
                question_4=request.POST['question_4'],
                question_5=request.POST['question_5'],
            )
            b2.save()
            return HttpResponse("Answers submitted!")
        else:
            return render(request, 'exercises/adverbs/B2.html')
    elif level == "C1":
        if request.method == 'POST':
            c1 = Questionnaire(
                level='C1',
                username=request.POST['username'],
                question_1=request.POST['question_1'],
                question_2=request.POST['question_2'],
                question_3=request.POST['question_3'],
                question_4=request.POST['question_4'],
                question_5=request.POST['question_5'],
            )
            c1.save()
            return HttpResponse("Answers submitted!")
        else:
            return render(request, 'exercises/adverbs/C1.html')
    else:
        return render(request, 'exercises/adverbs.html')


def results(request):
    unique_users = get_unique_usernames(Questionnaire.objects.all())
    table = QuestionnaireTable(Questionnaire.objects.all())

    return render_to_response("exercises/results.html", {"table": table},
                              context_instance=RequestContext(request))

