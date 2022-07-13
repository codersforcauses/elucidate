from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .serializers import *

from django.views.decorators.csrf import csrf_exempt  # will change this later


@csrf_exempt
def QuestionTask(request):
    if(request.method == 'GET'):    
        question = Quiz_Question.objects.all()
        serializer = Quiz_QuestionSerializer(question, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = Quiz_QuestionSerializer(data=data)
        if(serializer.is_valid(raise_exception=True)):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    else:
        return HttpResponse(status=400)  # bad request

@csrf_exempt
def SpecificQuestionTask(request, question_pk):
    question = get_object_or_404(Quiz_Question, pk=question_pk)
    
    if(request.method == 'GET'):
        serializer = Quiz_QuestionSerializer(question)
        return JsonResponse(serializer.data)
    else:
        return HttpResponse(status=400)  # bad request

@csrf_exempt
def AnswerTask(request, question_pk):
    question = get_object_or_404(Quiz_Question, pk=question_pk)
    
    if(request.method == 'GET'):
        answers = question.question_answer_set.all()
        serializer = Question_AnswerSerializer(answers, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = Question_AnswerSerializer(data=data)
        if(serializer.is_valid(raise_exception=True)):
            question.question_answer_set.create(is_correct=serializer.data['is_correct'], answer=serializer.data['answer'])
            return JsonResponse(serializer.data, status=201)
    else:
        return HttpResponse(status=400)  # bad request

@csrf_exempt
def SpecificAnswerTask(request, question_pk, answer_pk):
    question = get_object_or_404(Quiz_Question, pk=question_pk)
    
    if(request.method == 'GET'):
        answer = get_object_or_404(Question_Answer, pk=answer_pk)
        serializer = Question_AnswerSerializer(answer)
        return JsonResponse(serializer.data)
    else:
        return HttpResponse(status=400)  # bad request

@csrf_exempt
def TagTask(request, question_pk):
    question = get_object_or_404(Quiz_Question, pk=question_pk)

    if(request.method == 'GET'):
        tags = question.question_tag_set.all()
        serializer = Question_TagSerializer(tags, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = Question_TagSerializer(data=data)
        if(serializer.is_valid(raise_exception=True)):
            question.question_tag_set.create(tag=serializer.data['tag'])
            return JsonResponse(serializer.data, status=201)
    else:
        return HttpResponse(status=400)  # bad request


