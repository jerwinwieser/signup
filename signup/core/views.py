from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse, reverse_lazy

from django.forms import inlineformset_factory, modelformset_factory
from django.shortcuts import render

from core import models
from core import forms

from bootstrap_modal_forms.generic import BSModalReadView, BSModalCreateView, BSModalDeleteView, BSModalFormView, BSModalUpdateView

redirect_view = 'survey_list'

class SurveyListView(ListView):
    model = models.Survey

class SurveyCreateView(BSModalCreateView):
    template_name = 'core/survey_create.html'
    form_class = forms.SurveyForm
    model = models.Survey
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy(redirect_view)

class SurveyUpdateView(BSModalUpdateView):
    template_name = 'core/survey_update.html'
    form_class = forms.SurveyForm
    model = models.Survey
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy(redirect_view)

class SurveyDeleteView(BSModalDeleteView):
    template_name = 'core/survey_delete.html'
    model = models.Survey
    success_message = 'Approach successfully deleted.'
    success_url = reverse_lazy(redirect_view)

class SurveyDetailView(DetailView):
    template_name = 'core/survey_detail.html'
    model = models.Survey

class QuestionCreateView(BSModalCreateView):
    template_name = 'core/question_create.html'
    form_class = forms.QuestionForm
    model = models.Question
    success_url = reverse_lazy(redirect_view)
    def get_initial(self):
        initial = super(QuestionCreateView, self).get_initial()
        initial['survey'] = self.kwargs.get('surv_id')
        return initial

class QuestionListView(ListView):
    model = models.Question
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        surv_id = self.kwargs.get('surv_id')
        print(surv_id)
        context['question_list'] = models.Question.objects.filter(survey_id=surv_id)
        return context

class QuestionUpdateView(BSModalUpdateView):
    template_name = 'core/question_update.html'
    model = models.Question
    form_class = forms.QuestionForm
    success_url = reverse_lazy(redirect_view)

class QuestionDeleteView(DeleteView):
    template_name = 'core/question_delete.html'
    model = models.Question
    fields = '__all__'
    success_url = reverse_lazy(redirect_view)

def SubmissionCreateView(request, surv_id):
    questions = models.Question.objects.filter(survey_id=surv_id)
    SubmissionFormSet = modelformset_factory(models.Submission, form=forms.SubmissionForm, extra=questions.count())
    initial_values = [{'question': id} for id in questions.values_list('pk', flat=True)]
    formset = SubmissionFormSet(queryset=models.Submission.objects.none(), initial=initial_values)

    question_pk = questions.values_list('pk', flat=True)
    question_text = questions.values_list('text', flat=True)
    question_type = questions.values_list('type', flat=True)

    if request.method == 'post':
        formset = SubmissionFormSet(request.POST)
        if formset.is_valid():
            index = 0
            for form in formset:
                question_id = question_pk[index]
                question = models.Question.objects.get(id=question_id)
                form.instance.question = question
                form.save()
                index += 1
            return render(request, 'core/submission_list.html')
    context = {
        'question_text': question_text,
        'question_type': question_type,
        'formset': formset,
    }
    return render(request, 'core/submission.html', context)

class SubmissionListView(ListView):
    model = models.Submission