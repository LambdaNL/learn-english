from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from .scorecalculator import *


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

def nouns(request, level):
    if request.method != 'POST' and level != '':
        return render_to_response('exercises/nouns/' + level + '.html',
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
                render_to_response('exercises/nouns/' + level + '.html',
                                   {'open_questions': models.OpenQuestion.objects.filter(category=level)},
                                   context_instance=RequestContext(request))

        return render_to_response('exercises/index.html', context_instance=RequestContext(request))
    else:
        return render(request, 'exercises/nouns/nouns.html')

def startQuestionNouns(request):
    models.OpenQuestion.objects.create(category="A1", question_1="I don't have much ... . (work)", answer="work")
    models.OpenQuestion.objects.create(category="A1", question_2="There are a lot of ... . (chair)", answer="chairs")
    models.OpenQuestion.objects.create(category="A1", question_3="The farmer loaded his cart with ... of fresh vegetables. (box)", answer="boxes")
    models.OpenQuestion.objects.create(category="A1", question_4="There are many ... . (beach)", answer="beaches")
    models.OpenQuestion.objects.create(category="A1", question_5="Do you like this kind of ... . (music)", answer="music")
    models.OpenQuestion.objects.create(category="A2", question_1="He quickly reads a ... . (book)", answer="book")
    models.OpenQuestion.objects.create(category="A2", question_2="Mandy is a pretty ... . (girl)", answer="girl")
    models.OpenQuestion.objects.create(category="A2", question_3="The class is loud ... . (today)", answer="today")
    models.OpenQuestion.objects.create(category="A2", question_4="Max is a good ... . (singer)", answer="singer")
    models.OpenQuestion.objects.create(category="A2", question_5="You can easily open this ... . (tin)", answer="tin")
    models.OpenQuestion.objects.create(category="B1", question_1="The ... on trees produce oxygen. (leave)", answer="leaves")
    models.OpenQuestion.objects.create(category="B1", question_2="I now pronounce you .... and wife (husband)", answer="husband")
    models.OpenQuestion.objects.create(category="B1", question_3="My .... gave me the wrong grade(teacher)", answer="teacher")
    models.OpenQuestion.objects.create(category="B1", question_4="... on the wall who is the prettiest of them all? (mirror)", answer="mirror")
    models.OpenQuestion.objects.create(category="B1", question_5="Do you like this kind of ... . (music)", answer="music")
    models.OpenQuestion.objects.create(category="B2", question_1="I set my ..... clock for 7am. (alarm)", answer="alarm")
    models.OpenQuestion.objects.create(category="B2", question_2="Cooking in a clean ... makes me happy (kitchen)", answer="kitchen")
    models.OpenQuestion.objects.create(category="B2", question_3="After 16 weeks of .... your belly would expand sooner (pregnant)", answer="pregnancy")
    models.OpenQuestion.objects.create(category="B2", question_4="... is the process of facilitating learning, or the acquisition of knowledge, skills, values, beliefs, and habits. (educate)", answer="education")
    models.OpenQuestion.objects.create(category="B2", question_5="Give me a proper ... for breaking up with me (reason)", answer="reason")
    models.OpenQuestion.objects.create(category="C1", question_1="You have to eat healthy  if you want to lose ... (weight)", answer="weight")
    models.OpenQuestion.objects.create(category="C1", question_1="... is better than curing (prevention)", answer="prevention")
    models.OpenQuestion.objects.create(category="C1", question_3="The farmer loaded his cart with ... of fresh vegetables. (box)", answer="boxes")
    models.OpenQuestion.objects.create(category="C1", question_4="Doctors have toc recognize the ... of diseases (sympton)", answer="symptons")
    models.OpenQuestion.objects.create(category="C1", question_5="Sperm ..... is the provision (or donation) by a male of his sper (donate)", answer="donation")


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

