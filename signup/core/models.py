from django.db import models
from django.utils import timezone

survey_description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2550, default=survey_description)
    def __str__(self):
        return self.title

class Question(models.Model):
    QUESTION_TYPES = (
        ('char_field', 'char_field'),
        ('text_field', 'text_field'),
    )
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True,  editable=True)
    type = models.CharField(max_length=255, choices=QUESTION_TYPES, default='text_field')
    text = models.TextField(max_length=2550)
    def __str__(self):
        return self.text

class Submission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False, editable=False)
    answer = models.TextField(max_length=2550)
    slug = models.SlugField(editable=False)
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(editable=False, default=timezone.now)
    def __str__(self):
        return self.slug
