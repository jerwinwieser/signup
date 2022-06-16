from urllib import request
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse, reverse_lazy

from django.forms import inlineformset_factory, modelformset_factory
from django.shortcuts import render

from core import models
from core import forms

import uuid

from bootstrap_modal_forms.generic import BSModalReadView, BSModalCreateView, BSModalDeleteView, BSModalFormView, BSModalUpdateView

from django.db.models import Count
from django_pivot.pivot import pivot
from django_pivot.histogram import histogram

redirect_view = 'survey_list'

class SurveyListView(ListView):
    model = models.Survey
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question_list'] = models.Question.objects.all()
        return context

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
        print(initial)
        return initial

class QuestionListView(ListView):
    model = models.Question
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        surv_id = self.kwargs.get('surv_id')
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

def submission_create(request, surv_id):
    questions = models.Question.objects.filter(survey_id=surv_id)
    SubmissionFormSet = modelformset_factory(models.Submission, form=forms.SubmissionForm, extra=questions.count())
    initial_values = [{'question': id} for id in questions.values_list('pk', flat=True)]
    formset = SubmissionFormSet(queryset=models.Submission.objects.none(), initial=initial_values)
    question_pk = questions.values_list('pk', flat=True)
    question_text = questions.values_list('text', flat=True)
    question_type = questions.values_list('type', flat=True)
    hash = uuid.uuid4().hex
    if request.method == 'POST':
        formset = SubmissionFormSet(request.POST)
        if formset.is_valid():
            index = 0
            for form in formset:
                question_id = question_pk[index]
                question = models.Question.objects.get(id=question_id)
                form.instance.hash = hash
                form.instance.slug = hash
                form.instance.question = question
                form.save()
                index += 1
            return render(request, 'core/submission_list.html')
    context = {
        'question_text': question_text,
        'question_type': question_type,
        'formset': formset,
    }
    return render(request, 'core/submission_create.html', context)

class SubmissionListView(ListView):
    model = models.Submission
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['survey_list'] = models.Survey.objects.all()
        context['question_list'] = models.Question.objects.all()
        set = models.Submission.objects.all().values('question__survey__title').annotate(count=Count('slug', distinct=True))
        print(set)
        context['set_list'] = set
        return context

class SubmissionListViewAggregate(ListView):
    model = models.Submission
    template_name = 'core/submission_list_aggregate.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        surv_id = self.kwargs.get('surv_id')
        set = models.Submission.objects.all().values('question__survey__title').annotate(count=Count('slug', distinct=True))
        survey_set = models.Submission.objects.filter(question__survey__id=surv_id)

        survery_set_distinct = models.Submission.objects.filter(question__survey__id=surv_id).values('slug').distinct()
        survery_set_distinct_name = models.Survey.objects.filter(id=surv_id).values('title').distinct()

        for record in survery_set_distinct:
            print(record)

        context['survery_set_distinct'] = survery_set_distinct
        context['survery_set_distinct_name'] = survery_set_distinct_name

        context['survey_list'] = models.Survey.objects.all()
        context['question_list'] = models.Question.objects.all()
        context['set_list'] = set
        context['survey_set_list'] = survey_set
        return context

# class SubmissionDetailView(DetailView):
#     template_name = 'core/submission_detail.html'
#     model = models.Submission
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         slug = self.kwargs.get('slug')
#         submission = models.Submission.objects.filter(slug=slug)
#         context['submission'] = submission
#         return context

def submission_detail(request, slug):
    submission = models.Submission.objects.filter(slug=slug)
    context = {
        'submission': submission,
    }
    return render(request, 'core/submission_detail.html', context)
