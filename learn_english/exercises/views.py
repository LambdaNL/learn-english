from django.http import HttpResponse
from django.shortcuts import render

from .models import Adverb


def index(request):
    return HttpResponse("index")


def Adverbs(request, level):
    if(level == "A1"):
        latest_question_list = Adverb.objects.all()
        context = {'question_list': latest_question_list}
        return render(request, 'exercises/ExerciseForm.html', context)
    elif(level == "A2"):
        return HttpResponse("Beginners level")
    elif (level == "B1"):
        return HttpResponse("Beginners level")
    elif (level == "B2"):
        return HttpResponse("Beginners level")
    elif (level == "C1"):
        return HttpResponse("Beginners level")
    else:
        return HttpResponse("This level doesn't exist")


def submit(request):
    a = request.POST['answer1']
    return HttpResponse(a)