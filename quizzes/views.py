from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request, 'quizzes/index.html')


def select(request):
    return render(request, 'quizzes/select.html')


def solve(request, quiz_id):
    return render(request, 'quizzes/solve.html')


def result(request, quiz_id):
    return render(request, 'quizzes/result.html')


def create(request):
    return render(request, 'quizzes/create.html')

