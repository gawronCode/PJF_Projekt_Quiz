from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import Quiz


def index(request):
    return render(request, 'quizzes/index.html')


def select(request):
    quizzes = Quiz.objects.order_by('-title')[:5]
    template = loader.get_template('quizzes/select.html')
    context = {
        'quizzes': quizzes
    }
    return HttpResponse(template.render(context, request))


def solve(request, quiz_id):
    return render(request, 'quizzes/solve.html')


def result(request, quiz_id):
    return render(request, 'quizzes/result.html')


def create(request):
    return render(request, 'quizzes/create.html')

