from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from .models import Questionnaire, QuestionnaireTable


def index(request):
    return HttpResponse("index")


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
            return render(request, 'exercises/A1.html')
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
            return render(request, 'exercises/A2.html')
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
            return render(request, 'exercises/B1.html')
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
            return render(request, 'exercises/B2.html')
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
            return render(request, 'exercises/C1.html')
    else:
        return HttpResponse("This level doesn't exist")


def results(request):
    unique_users = get_unique_usernames(Questionnaire.objects.all())
    table = QuestionnaireTable(Questionnaire.objects.all())

    return render_to_response("exercises/results.html", {"table": table},
                              context_instance=RequestContext(request))


def get_unique_usernames(results):
    usernames = []
    for result in results:
        usernames += result.username
    return set(usernames)


def calculate_scores(unique_users):

    for user in unique_users:
        user_results = Questionnaire.objects.filter(username=user)
        total_score = 0
        for user_result in user_results:
            if user_result.level == "A1":
                total_score += evaluate_A1(user_result)
            if user_result.level == "A2":
                total_score += evaluate_A2(user_result)
            if user_result.level == "B1":
                total_score += evaluate_B1(user_result)
            if user_result.level == "B2":
                total_score += evaluate_B2(user_result)
            if user_result.level == "C1":
                total_score += evaluate_C1(user_result)


def evaluate_A1(answers):
    score = 0
    if answers.question_1 == "quickly":
        score += 1
    if answers.question_2 == "pretty":
        score += 1
    if answers.question_3 == "terribly":
        score += 1
    if answers.question_4 == "good":
        score += 1
    if answers.question_5 == "easily":
        score += 1
    return score


def evaluate_A2(answers):
    # TODO:
    pass


def evaluate_B1(answers):
    # TODO:
    pass


def evaluate_B2(answers):
    # TODO:
    pass


def evaluate_C1(answers):
    # TODO:
    pass
