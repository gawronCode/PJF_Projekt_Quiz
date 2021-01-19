from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse('Strona powitalna aplikacji quizowej')


def select(request):
    return HttpResponse('Strona zawierająca spis quizów do rozwiązania')


def solve(request, quiz_id):
    return HttpResponse('strona na której rozwiązuje się quiz o nazwie %s.' % quiz_id)


def result(request, quiz_id):
    return HttpResponse('strona pokazujący wynik uzyskany po rozwiązaniu quizu %s.' % quiz_id)


def create(request):
    return HttpResponse('strona do tworzenia nowego quizu')

