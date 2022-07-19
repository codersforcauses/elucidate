from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Quiz_Question
from rest_framework.status import (
                                    HTTP_201_CREATED,
                                    HTTP_400_BAD_REQUEST,
                                    HTTP_204_NO_CONTENT)
from .serializers import (
                            QuestionInfoSerializer,
                            Quiz_QuestionSerializer,
                            Question_AnswerSerializer,
                            Question_TagSerializer)


from django.views.decorators.csrf import csrf_exempt  # will change this later


@csrf_exempt
@api_view(['GET', 'POST'])
def QuestionTask(request):
    if request.method == 'GET':
        question = Quiz_Question.objects.all()
        serializer = Quiz_QuestionSerializer(question, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif(request.method == 'POST'):
        serializer = QuestionInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            q = Quiz_Question(
                question=serializer.data['question'],
                question_type=serializer.data['question_type'],
                date_created=serializer.data['date_created'])
            q.save()
            for tag in serializer.data['tags']:
                q.question_tag_set.create(tag=tag)
            return JsonResponse(
                                    Quiz_QuestionSerializer(q).data,
                                    status=HTTP_201_CREATED)

    else:
        return HttpResponse(status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def SpecificQuestionTask(request, q_pk):
    question = get_object_or_404(Quiz_Question, pk=q_pk)

    if(request.method == 'GET'):
        serializer = Quiz_QuestionSerializer(question)
        return JsonResponse(serializer.data)

    elif(request.method == 'PUT'):
        serializer = Quiz_QuestionSerializer(
                                                question,
                                                data=request.data,
                                                partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)

    elif(request.method == 'DELETE'):
        question.delete()
        return HttpResponse(status=HTTP_204_NO_CONTENT)

    else:
        return HttpResponse(status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
def AnswerTask(request, q_pk):
    question = get_object_or_404(Quiz_Question, pk=q_pk)

    if(request.method == 'GET'):
        answers = question.question_answer_set.all()
        serializer = Question_AnswerSerializer(answers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif(request.method == 'POST'):
        serializer = Question_AnswerSerializer(data=request.data)
        if(serializer.is_valid(raise_exception=True)):
            question.question_answer_set.create(
                                    is_correct=serializer.data['is_correct'],
                                    answer=serializer.data['answer'])
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)

    else:
        return HttpResponse(status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def SpecificAnswerTask(request, q_pk, a_pk):
    question = get_object_or_404(Quiz_Question, pk=q_pk)
    answer = get_object_or_404(question.question_answer_set, pk=a_pk)

    if(request.method == 'GET'):
        serializer = Question_AnswerSerializer(answer)
        return JsonResponse(serializer.data)

    elif(request.method == 'PUT'):
        serializer = Question_AnswerSerializer(
                                                answer,
                                                data=request.data,
                                                partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)

    elif(request.method == 'DELETE'):
        answer.delete()
        return HttpResponse(status=HTTP_204_NO_CONTENT)

    else:
        return HttpResponse(status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
def TagTask(request, q_pk):
    question = get_object_or_404(Quiz_Question, pk=q_pk)

    if(request.method == 'GET'):
        tags = question.question_tag_set.all()
        serializer = Question_TagSerializer(tags, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif(request.method == 'POST'):
        serializer = Question_TagSerializer(data=request.data)
        if(serializer.is_valid(raise_exception=True)):
            question.question_tag_set.create(tag=serializer.data['tag'])
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)

    else:
        return HttpResponse(status=HTTP_400_BAD_REQUEST)
