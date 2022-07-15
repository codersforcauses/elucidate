from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from .serializers import *
from .models import *


# Handle GET requests for general info about a Quiz
@csrf_exempt
def quiz(request, quiz_pk):
    quiz = get_object_or_404(Quiz, pk=quiz_pk)

    if request.method == "GET":
        serializer = QuizSerializer(quiz)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=400)


# Handle GET requests for Objectives of a particular Quiz
@csrf_exempt
def objectives(request, quiz_pk):
    objectives = Objective.objects.get(quiz__pk=quiz_pk)

    if request.method == "GET":
        serializer = ObjectiveSerializer(objectives, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=400)


# Handle GET requests for Tags of a particular Quiz
@csrf_exempt
def tags(request, quiz_pk):
    tags = Tag.objects.get(quiz__pk=quiz_pk)

    if request.method == "GET":
        serializer = TagSerializer(tags, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=400)


# Handle GET requests for a particular Question of a particular Quiz
@csrf_exempt
def question(request, quiz_pk, question_pk):
    question = get_object_or_404(Question, quiz__pk=quiz_pk, pk=question_pk)

    if request.method == "GET":
        serializer = QuestionSerializer(question)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=400)
    

# Handle GET requests for Answers of a particular Question of a particular Quiz
@csrf_exempt
def answers(request, quiz_pk, question_pk):
    answers = Answer.objects.get(question__pk=question_pk,
                                 question__quiz__pk=quiz_pk)

    if request.method == "GET":
        serializer = AnswerSerializer(answers, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=400)

