from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import QuestionInfoSerializer
from api.apps.shared_models.models import quiz_models
from api.apps.shared_models.serializers import quiz_serializers

from django.views.decorators.csrf import csrf_exempt  # will change this later


@csrf_exempt
@api_view(['GET', 'POST'])
def QuestionTask(request):
    if request.method == 'GET':
        question = quiz_models.Question.objects.all()
        serializer = quiz_serializers.QuestionSerializer(question, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = QuestionInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            question = quiz_models.Question(
                text=serializer.data['text'],
                question_type=serializer.data['question_type'],
                date_created=serializer.data['date_created'])
            question.save()

            for answer in serializer.data['answers']:
                # vaildate fields as the serialiser doesn't verify them
                if type(answer[0]) is str and type(answer[1]) is bool:
                    question.answer_set.create(
                        text=answer[0],
                        is_correct=answer[1])
                else:
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

            for name in serializer.data['tags']:
                question.tag_set.create(name=name)

            return JsonResponse(
                quiz_serializers.QuestionSerializer(question).data,
                status=status.HTTP_201_CREATED)

    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def SpecificQuestionTask(request, q_pk):
    question = get_object_or_404(quiz_models.Question, pk=q_pk)

    if request.method == 'GET':
        serializer = quiz_serializers.QuestionSerializer(question)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = quiz_serializers.QuestionSerializer(
            question,
            data=request.data,
            partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        question.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
def AnswerTask(request, q_pk):
    question = get_object_or_404(quiz_models.Question, pk=q_pk)

    if request.method == 'GET':
        answers = question.answer_set.all()
        serializer = quiz_serializers.AnswerSerializer(answers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = quiz_serializers.AnswerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            question.answer_set.create(
                text=serializer.data['text'],
                is_correct=serializer.data['is_correct'])
            return JsonResponse(
                serializer.data,
                status=status.HTTP_201_CREATED)

    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def SpecificAnswerTask(request, q_pk, a_pk):
    question = get_object_or_404(quiz_models.Question, pk=q_pk)
    answer = get_object_or_404(question.answer_set, pk=a_pk)

    if request.method == 'GET':
        serializer = quiz_serializers.AnswerSerializer(answer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = quiz_serializers.AnswerSerializer(
                                                answer,
                                                data=request.data,
                                                partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        answer.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
def TagTask(request, q_pk):
    question = get_object_or_404(quiz_models.Question, pk=q_pk)

    if request.method == 'GET':
        tags = question.tag_set.all()
        serializer = quiz_serializers.TagSerializer(tags, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = quiz_serializers.TagSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            question.tag_set.create(name=serializer.data['name'])
            return JsonResponse(
                serializer.data,
                status=status.HTTP_201_CREATED)

    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
