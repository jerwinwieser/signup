from django.db import models
from django.utils import timezone

survey_description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'

class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2500, default=survey_description)
    def __str__(self):
        return self.title

class Question(models.Model):
    TYPES = (
        ('char_field', 'char_field'),
        ('text_field', 'text_field'),
    )
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True,  editable=True)
    dtype = models.CharField(max_length=200, choices=TYPES, default='text')
    def __str__(self):
        return self.text

class Datatype(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False, editable=False)
    char_field = models.CharField(max_length=2550, null=True)
    text_field = models.TextField(null=True)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=2048, null=False, blank=False)

class Submission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False, editable=False)
    answer = models.CharField(max_length=2550)
    slug = models.SlugField(editable=False)
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(editable=False, default=timezone.now)
    def __str__(self):
        return self.slug
