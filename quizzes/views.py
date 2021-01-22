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


def add_question(request, quiz_id):
    question_contents = request.POST.get('questionContents', 'none')

    if question_contents == 'none':
        response = redirect('edit', quiz_id)
        return response

    new_question = Question(contents=question_contents, quiz_id=quiz_id)
    new_question.save()

    response = redirect('edit_question', new_question.id)
    return response


def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question_quiz_id = question.quiz_id
    question.delete()
    response = redirect('edit', question_quiz_id)
    return response


def edit_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    template = loader.get_template('quizzes/edit_question.html')
    context = {
        'question': question,
        'quiz_id': question.quiz_id
    }
    return HttpResponse(template.render(context, request))


def add_answer(request, question_id):
    answer_contents = request.POST.get('answerContents', 'none')
    answer_is_true = request.POST.get('answerIsTrue', 'none')

    if answer_contents == 'none':
        response = redirect('edit_question', question_id)
        return response

    new_answer = Answer(contents=answer_contents,
                        is_true=(lambda x: True if x == 'True' else False)(answer_is_true),
                        question_id=question_id)

    new_answer.save()

    response = redirect('edit_question', new_answer.question_id)
    return response


def delete_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    question_id = answer.question_id
    answer.delete()
    response = redirect('edit_question', question_id)
    return response


def update_answer(request, answer_id):

    answer_to_update = get_object_or_404(Answer, id=answer_id)

    answer_contents = request.POST.get('answerContents', 'none')
    answer_is_true = request.POST.get('answerIsTrue', 'none')

    if answer_contents == 'none':
        response = redirect('edit_question', answer_to_update.question_id)
        return response

    answer_to_update.contents = answer_contents
    answer_to_update.is_true = (lambda x: True if x == 'True' else False)(answer_is_true)
    answer_to_update.save()

    response = redirect('edit_question', answer_to_update.question_id)
    return response
