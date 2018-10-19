from rest_framework import status

from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.response import Response

from .serializers import InputAnswersSerializer, QuestionsSerializer, InputUserSerializer
from .models import Input_Answer, Input_Title, Input_User, Question, Project

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


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

class InputUserCreate(CreateAPIView):
    queryset = Input_User.objects.all()
    serializer_class = InputUserSerializer


"""
API for saving answers to database. 
"""
class AnswersCreate(CreateAPIView):
    queryset = Input_Answer.objects.all()
    serializer_class = InputAnswersSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = InputAnswersSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            response = "done"
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

"""
API for listing answers from database. 
"""
class AnswersList(ListAPIView):
    queryset = Input_Answer.objects.all()
    serializer_class = InputAnswersSerializer

"""
API for listing questions with nested information. 
"""
class QuestionsList(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer
