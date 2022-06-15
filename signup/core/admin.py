from django.contrib import admin
from core import models

admin.site.register(models.Survey)
admin.site.register(models.Question)
admin.site.register(models.Submission)