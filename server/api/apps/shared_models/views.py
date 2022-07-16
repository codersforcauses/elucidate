from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from .serializers import *
from .models import *


# Handle GET requests for a particular Question
@csrf_exempt
def question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)

    if request.method == "GET":
        serializer = QuestionSerializer(question)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=400)
    

# Handle GET requests for Tags of a particular Quiz
@csrf_exempt
def tags(request, question_pk):
    tags = Tag.objects.get(question__pk=question_pk)

    if request.method == "GET":
        serializer = TagSerializer(tags, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=400)


# Handle GET requests for Answers of a particular Question of a particular Quiz
@csrf_exempt
def answers(request, question_pk):
    answers = Answer.objects.get(question__pk=question_pk)

    if request.method == "GET":
        serializer = AnswerSerializer(answers, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=400)

