from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

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
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    template = loader.get_template('quizzes/result.html')
    answers = []

    questions = quiz.question_set.all()

    for question in questions:
        x = request.POST.get('answer{}'.format(question.id), 'none')

        if x == 'none':
            context = {
                'error_message': 'Nie udzielono odpowiedzi na wszystkie pytania :(',
            }
            return HttpResponse(template.render(context, request))
        else:
            answers.append((lambda x: True if x == 'True' else False)(x))

    correct_answers = 0
    total_answers = 0

    for answer in answers:
        total_answers += 1
        if answer:
            correct_answers += 1
        elif answer is None:
            context = {
                'error_message': 'Nie udzielono odpowiedzi na wszystkie pytania.',
            }
            return HttpResponse(template.render(context, request))

    context = {
        'correct_answers': correct_answers,
        'total_answers': total_answers,
    }
    return HttpResponse(template.render(context, request))


def manage(request):
    quizzes = Quiz.objects.only()[:]
    template = loader.get_template('quizzes/manage.html')
    context = {
        'quizzes': quizzes
    }
    return HttpResponse(template.render(context, request))


def create(request):

    quiz_name = request.POST.get('quizName', 'none')

    if quiz_name == 'none':
        response = redirect('manage')
        return response

    new_quiz = Quiz(title=quiz_name)
    new_quiz.save()

    new_quiz_id = new_quiz.id

    response = redirect('edit', new_quiz_id)
    return response


def delete(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    quiz.delete()
    response = redirect('manage')
    return response


def edit(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    template = loader.get_template('quizzes/edit.html')
    context = {
        'quiz': quiz,
    }
    return HttpResponse(template.render(context, request))

