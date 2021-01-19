from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    contents = models.CharField(max_length=512)

    def __str__(self):
        return self.contents


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    contents = models.CharField(max_length=512)
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.contents
