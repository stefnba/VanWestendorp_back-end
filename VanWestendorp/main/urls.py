from django.urls import path

from . import views
from .views import AnswersCreate, AnswersList

app_name = "main"

urlpatterns = [
    path('', views.index, name='index'),

    path('answers/create/', AnswersCreate.as_view(), name='answers-create'),
    path('answers/', AnswersList.as_view(), name='answers-list'),
]