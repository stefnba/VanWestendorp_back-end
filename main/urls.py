from django.urls import path

from . import views
from .views import AnswersCreate, AnswersList, QuestionsList, InputUserCreate

app_name = "main"

urlpatterns = [
    path('', views.index, name='index'),

    path('questions/', QuestionsList.as_view(), name='questions-list'),
    path('answers/create/', AnswersCreate.as_view(), name='answers-create'),
    path('input/create/', InputUserCreate.as_view(), name='input-create'),
    path('answers/', AnswersList.as_view(), name='answers-list'),
]