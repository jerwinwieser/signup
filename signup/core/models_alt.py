from django.db import models
from django.utils import timezone

survey_description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'

class Quiz(models.Model):
    name = models.CharField(max_length=2048, null=False, blank=False)

class Question(models.Model):
    TYPES = (
        (1, 'radio'),
        (2, 'checkbox'),
        (3, 'text'),
    )
    quiz = models.ForeignKey(Quiz)
    type = models.CharField(max_length=8, choices=TYPES, default='radio')
    prompt = models.CharField(max_length=2048, null=False, blank=False)
    correct_free_text = models.CharField(max_length=2048, null=True, blank=True)
    rank = models.SmallIntegerField(default=0)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=2048, null=False, blank=False)
    correct = models.BooleanField(default=False)
    rank = models.SmallIntegerField(default=0)

class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, null=True, on_delete=models.DO_NOTHING)
    free_text = models.CharField(max_length=2048, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)