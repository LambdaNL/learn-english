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

#gerund
def gerund(request, level):
    print(level)
    if request.method != 'POST' and level != '':
        return render_to_response('exercises/gerund/' + level + '.html',
                                  {'open_questions': models.OpenQuestion.objects.filter(category=str(level))},
                                  context_instance=RequestContext(request))

    elif request.method == 'POST':
        for q in models.OpenQuestion.objects.filter(category=str(level)):
            if request.POST[str(q.pk)] != '':
                foq = models.FilledOpenQuestion(
                    username=request.POST['username'],
                    question=q.question,
                    answer=request.POST[str(q.pk).lower()])
                foq.save()
            else:
                render_to_response('exercises/gerund/' + level + '.html',
                                   {'open_questions': models.OpenQuestion.objects.filter(category=level)},
                                   context_instance=RequestContext(request))

        return render_to_response('exercises/index.html', context_instance=RequestContext(request))
    else:
        return render(request, 'exercises/gerund/gerund.html')

def results(request):
    unique_users = get_unique_usernames(models.FilledOpenQuestion.objects.all())

    for user in unique_users:

        if len(models.UserScore.objects.filter(username=user)) == 0:
            models.UserScore.objects.create(username=user, totalCorrect=0, totalIncorrect=0, score=0)

        else:
            correct_amount = get_correct_amount(user)
            incorrect_amount = get_incorrect_amount(user)
            score = correct_amount - incorrect_amount
            models.UserScore.objects.filter(username=user).update(totalCorrect=correct_amount,
                                                                  totalIncorrect=incorrect_amount,
                                                                  score=score)

    return render_to_response("exercises/results.html", {"users": models.UserScore.objects.all()},
                              context_instance=RequestContext(request))


def startg(request):
    models.OpenQuestion.objects.create(category="A1" , question="My friend is good ... playing volleyball." , answer="at")
    models.OpenQuestion.objects.create(category="A1" , question="She complains ... playing volleyball.", answer="about")
    models.OpenQuestion.objects.create(category="A1" , question="They are afraid ... losing the match." , answer="of")
    models.OpenQuestion.objects.create(category="A1" , question="She doesn't feel ... working on the computer." , answer="like")
    models.OpenQuestion.objects.create(category="A1" , question="We are looking forward ... going out in the weekend.", answer="to")
    # models.gOpenQuestion.objects.create(level="A2" , question=1, answer="losing")
    # models.gOpenQuestion.objects.create(level="A2" , question=2, answer="seeing")
    # models.gOpenQuestion.objects.create(level="A2" , question=3, answer="collecting")
    # models.gOpenQuestion.objects.create(level="A2" , question=4, answer="going")
    # models.gOpenQuestion.objects.create(level="A2" , question=5, answer="waiting")
    # models.gOpenQuestion.objects.create(level="B1" , question=1, answer="of")
    # models.gOpenQuestion.objects.create(level="B1" , question=2, answer="of")
    # models.gOpenQuestion.objects.create(level="B1" , question=3, answer="of")
    # models.gOpenQuestion.objects.create(level="B1" , question=4, answer="on")
    # models.gOpenQuestion.objects.create(level="B1" , question=5, answer="on")
    # models.gOpenQuestion.objects.create(level="B2" , question=1, answer="at")
    # models.gOpenQuestion.objects.create(level="B2" , question=2, answer="of")
    # models.gOpenQuestion.objects.create(level="B2" , question=3, answer="about")
    # models.gOpenQuestion.objects.create(level="B2" , question=4, answer="of")
    # models.gOpenQuestion.objects.create(level="B2" , question=5, answer="in")
    # models.gOpenQuestion.objects.create(level="C1" , question=1, answer="going")
    # models.gOpenQuestion.objects.create(level="C1" , question=2, answer="to buy")
    # models.gOpenQuestion.objects.create(level="C1" , question=3, answer="to get")
    # models.gOpenQuestion.objects.create(level="C1" , question=4, answer="seeing")
    # models.gOpenQuestion.objects.create(level="C1" , question=5, answer="to run")
    
    return HttpResponse("Answers for Gerund added to DB!")
