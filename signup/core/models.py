from django.db import models
import uuid
import time
import hashlib

#one user should be able to create multiple surveys
class Survey(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

#one survey can have multiple questions
class Question(models.Model):
    CHARFIELD = "charfield"
    INTEGERFIELD = "integerfield"
    QUESTION_TYPES = (
        (CHARFIELD, ("charfield")),
        (INTEGERFIELD, ("integerfield")),
    )
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True,  editable=False)
    type = models.CharField(max_length=200, choices=QUESTION_TYPES, default=CHARFIELD)
    text = models.CharField(max_length=255)
    def __str__(self):
        return self.text

#one question can have multiple submissions
#one answer can have multiple submissions and one submission can have multiple answers
class Submission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False, editable=False)
    answer = models.CharField(max_length=255)
    # bash = models.CharField(max_length=10, default='defaulthash', unique=False)
    def __str__(self):
        return self.answer
