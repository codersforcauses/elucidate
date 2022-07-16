from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.status import *
from rest_framework.decorators import api_view
from .serializers import *

from django.views.decorators.csrf import csrf_exempt  # will change this later


@csrf_exempt
@api_view(['GET', 'POST'])
def QuestionTask(request):
    if(request.method == 'GET'):    
        question = Quiz_Question.objects.all()
        serializer = Quiz_QuestionSerializer(question, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif(request.method == 'POST'):
        serializer = Quiz_QuestionSerializer(data=request.data)
        if(serializer.is_valid(raise_exception=True)):
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    else:
        return HttpResponse(status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def SpecificQuestionTask(request, question_pk):
    question = get_object_or_404(Quiz_Question, pk=question_pk)
    
    if(request.method == 'GET'):
        serializer = Quiz_QuestionSerializer(question)
        return JsonResponse(serializer.data)

    elif(request.method == 'PUT'):
        serializer = Quiz_QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)
    
    elif(request.method == 'DELETE'):
        question.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    else:
        return HttpResponse(status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])
def AnswerTask(request, question_pk):
    question = get_object_or_404(Quiz_Question, pk=question_pk)
    
    if(request.method == 'GET'):
        answers = question.question_answer_set.all()
        serializer = Question_AnswerSerializer(answers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif(request.method == 'POST'):
        serializer = Question_AnswerSerializer(data=request.data)
        if(serializer.is_valid(raise_exception=True)):
            question.question_answer_set.create(is_correct=serializer.data['is_correct'], answer=serializer.data['answer'])
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
    
    else:
        return HttpResponse(status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def SpecificAnswerTask(request, question_pk, answer_pk):
    question = get_object_or_404(Quiz_Question, pk=question_pk)
    answer = get_object_or_404(question.question_answer_set, pk=answer_pk)
    
    if(request.method == 'GET'):
        # answer = get_object_or_404(Question_Answer, pk=answer_pk)
        serializer = Question_AnswerSerializer(answer)
        return JsonResponse(serializer.data)

    elif(request.method == 'PUT'):
        # answer = get_object_or_404(Question_Answer, pk=answer_pk)
        serializer = Question_AnswerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)
    
    elif(request.method == 'DELETE'):
        answer.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
    else:
        return HttpResponse(status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])
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
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
    
    else:
        return HttpResponse(status=HTTP_400_BAD_REQUEST)


