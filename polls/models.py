from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=64)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    contents = models.CharField(max_length=512)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    contents = models.CharField(max_length=512)
    is_true = models.BooleanField(default=False)
