from django.urls import path

from . import views
from .views import (
    AnswersList, 
    QuestionsList, 
    InputUserCreate, 
    OutputQuestion, 
    ProjectsList,
    ProjectQuestionsList
)

app_name = "main"

urlpatterns = [
    path('', views.index, name='index'),

    # questions
    path('questions/', QuestionsList.as_view(), name='questions-list'),
    
    path('answers/', AnswersList.as_view(), name='answers-list'),

    # create new user input (answers with M2M relation)
    path('input/create/', InputUserCreate.as_view(), name='input-create'),
    
    # output
    path('output/question/<int:pk>/', OutputQuestion.as_view(), name='output-question'),

    # projects
    path('projects/', ProjectsList.as_view(), name='projects-list'),
    path('project/<int:project>/questions/', ProjectQuestionsList.as_view(), name='project-question-list'),


]