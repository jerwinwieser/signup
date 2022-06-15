from django.urls import path
from core import views

urlpatterns = [
    path('', views.SurveyListView.as_view(), name='survey_list'),
    path('survey/create/', views.SurveyCreateView.as_view(), name='survey_create'),
    path('survey/update/<int:pk>', views.SurveyUpdateView.as_view(), name='survey_update'),
    path('survey/detail/<int:pk>', views.SurveyDetailView.as_view(), name='survey_detail'),
    path('survey/delete/<int:pk>', views.SurveyDeleteView.as_view(), name='survey_delete'),

    path('question/create/<int:surv_id>', views.QuestionCreateView.as_view(), name='question_create'),
    path('question/list/<int:surv_id>/', views.QuestionListView.as_view(), name='question_list'),
    path('question/update/<int:pk>', views.QuestionUpdateView.as_view(), name='question_update'),
    path('question/delete/<int:pk>', views.QuestionDeleteView.as_view(), name='question_delete'),

    path('submission/list/', views.SubmissionListView.as_view(), name='submission_list'),
    path('submission/create/<int:surv_id>/', views.submission_create, name='submission_create'),
]
