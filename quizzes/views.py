from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

from .models import Quiz, Question, Answer


def index(request):
    return render(request, 'quizzes/index.html')


def select(request):
    quizzes = Quiz.objects.only()[:]
    template = loader.get_template('quizzes/select.html')
    context = {
        'quizzes': quizzes
    }
    return HttpResponse(template.render(context, request))


def solve(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    template = loader.get_template('quizzes/solve.html')
    context = {
        'quiz': quiz,
    }
    return HttpResponse(template.render(context, request))


def result(request, quiz_id):
    return render(request, 'quizzes/result.html')


def create(request):
    return render(request, 'quizzes/create.html')

