from rest_framework import status

from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from .serializers import AnswersSerializer
from .models import Answers

from django.http import HttpResponse








def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class AnswersCreate(CreateAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = AnswersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("yes", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class AnswersList(ListAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer