from django.http import HttpResponse


def index(request):
    return HttpResponse("index")


def A1(request):
    return HttpResponse("A1")


def A2(request):
    return HttpResponse("A2")


def B1(request):
    return HttpResponse("B1")


def B2(request):
    return HttpResponse("B2")


def C1(request):
    return HttpResponse("C1")

