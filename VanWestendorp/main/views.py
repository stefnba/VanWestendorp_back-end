from rest_framework import status

from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import (
    Input_Answer, 
    Input_Title, 
    Input_User, 
    Question, 
    Project
)

from .serializers import (
    ProjectListSerializer, 
    InputAnswersSerializer, 
    QuestionListSerializer, 
    InputUserSerializer, 
    InputListSerializer, 
    OutputQuestionSerializer
)


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, there is nothing here for you :-)")


""" Projects """

# Simple list of all active projects, no nested infos
class ProjectsList(ListAPIView):
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectListSerializer

class ProjectQuestionsList(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer

    # override queryset to filter for question from url
    def get_queryset(self):
        project = self.kwargs['project']
        return Question.objects.filter(project=project)

""" Questions """

# API for listing questions with nested information on input fields. 
class QuestionsList(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer


""" Answers """

# list all plain answers, no added or nested info
class AnswersList(ListAPIView):
    queryset = Input_Answer.objects.all()
    serializer_class = InputAnswersSerializer



""" Output """

# Retrieve one question with nested input fields and corresponding answers
# Already parsed for output
class OutputQuestion(RetrieveAPIView):    
    queryset = Question.objects.all()
    serializer_class = OutputQuestionSerializer


""" User input """

# save user input in database (considering M2M relation)
class InputUserCreate(CreateAPIView):
    queryset = Input_User.objects.all()
    serializer_class = InputUserSerializer



















# class OutputQuestion(RetrieveAPIView):    
#     queryset = Question.objects.all()
#     serializer_class = OutputQuestionSerializer
    # lookup_field = 'id'

    # override queryset to filter for question from url
    # def get_queryset(self):
    #     question = self.kwargs['question']
    #     return Input_Title.objects.filter(question=question)


# class AnswersCreate(CreateAPIView):
#     queryset = Answers.objects.all()
#     serializer_class = AnswersSerializer

#     def create(self, request, *args, **kwargs):
#         print(request.data)

#         name = request.data['name']
#         translationTable = str.maketrans("éàèùâêîôûçäöü", "eaeuaeioucaou")
#         name = name.translate(translationTable)

#         serializer = AnswersSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save(name=name)
#             return Response("yes", status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# class AnswersCreate(CreateAPIView):
#     queryset = Input_Answer.objects.all()
#     serializer_class = InputAnswersSerializer

#     def create(self, request, *args, **kwargs):
#         print(request.data)
#         serializer = InputAnswersSerializer(data=request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             response = "done"
#             return Response(response, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)