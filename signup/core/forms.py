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

class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['type'] = 'text'

class TypeForm(forms.ModelForm):
    class Meta:
        model = models.Type
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['type'] = 'text'

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = models.Submission
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(SubmissionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['type'] = 'text'

# class SubmissionForm(forms.Form):
#     CITIES = (
#         (1, 'lisbon'),
#         (2, 'amsterdam'),
#         (3, 'fortaleza'),
#     )
#     name = forms.CharField(max_length=2550)
#     age = forms.IntegerField()
#     city = forms.ChoiceField(choices=CITIES)
