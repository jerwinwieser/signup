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
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            # visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['class'] = 'form-select'
            visible.field.widget.attrs['type'] = 'text'
            # visible.field.widget.attrs['placeholder'] = 'Placeholder'

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = models.Submission
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(SubmissionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['type'] = 'text'
            # visible.field.widget.attrs['placeholder'] = 'Placeholder'
