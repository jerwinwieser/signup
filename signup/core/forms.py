from random import choices
from django import forms
from core import models
from django.forms import inlineformset_factory, modelformset_factory
from bootstrap_modal_forms.forms import BSModalModelForm

class SurveyForm(BSModalModelForm):
    class Meta:
        model = models.Survey
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['type'] = 'text'
            visible.field.widget.attrs['placeholder'] = 'Placeholder'

class QuestionForm(BSModalModelForm):
    class Meta:
        model = models.Question
        fields = '__all__'

FIELDS = {
    models.Question.TEXT: forms.CharField,
    models.Question.SHORT_TEXT: forms.CharField,
}
WIDGETS = {
    models.Question.TEXT: forms.Textarea,
    models.Question.SHORT_TEXT: forms.TextInput,
}

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = models.Submission
        fields = '__all__'
    def get_question_widget(self, question):
        """Return the widget we should use for a question.
        :param Question question: The question
        :rtype: django.forms.widget or None"""
        try:
            return self.WIDGETS[question.type]
        except KeyError:
            return None