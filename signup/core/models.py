from django.db import models
from django.utils import timezone

survey_description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'

#one user should be able to create multiple surveys
class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2500, default=survey_description)
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
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True,  editable=True)
    type = models.CharField(max_length=200, choices=QUESTION_TYPES, default=CHARFIELD)
    text = models.CharField(max_length=2500)
    def __str__(self):
        return self.text

#one question can have multiple submissions
#one answer can have multiple submissions and one submission can have multiple answers
class Submission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False, editable=False)
    # answer = models.TextField(max_length=2500)
    answer = models.CharField(max_length=2500)
    slug = models.SlugField(editable=False)
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(editable=False, default=timezone.now)
    def __str__(self):
        return self.slug
