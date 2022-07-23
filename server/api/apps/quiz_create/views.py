from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import QuestionInfoSerializer
from api.apps.shared_models.models import quiz_models
from api.apps.shared_models.serializers import quiz_serializers


# this method associates a tag with a question or adds a new tag to the
# database and returns the Tag object
def AddTagToQuestion(question, tag_name):
    try:
        tag = quiz_models.Tag.objects.get(name=tag_name)
        question.tag_set.add(tag)
    except quiz_models.Tag.DoesNotExist:
        tag = question.tag_set.create(name=tag_name)
    except quiz_models.Tag.MultipleObjectsReturned:
        # hopefully this shouldn't be executed in production
        tag = quiz_models.Tag.objects.filter(name=tag_name)[0]
        question.tag_set.add(tag)
    return tag


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

            if 'answers' in serializer.data:
                for answer in serializer.data['answers']:
                    # vaildate fields as the serialiser doesn't verify them
                    if type(answer[0]) is str and type(answer[1]) is bool:
                        question.answer_set.create(
                            text=answer[0],
                            is_correct=answer[1])
                    else:
                        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

            for name in serializer.data['tags']:
                AddTagToQuestion(question, name)

            return JsonResponse(
                quiz_serializers.QuestionSerializer(question).data,
                status=status.HTTP_201_CREATED)

    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


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
            answer = question.answer_set.create(
                text=serializer.data['text'],
                is_correct=serializer.data['is_correct'])
            return JsonResponse(
                quiz_serializers.AnswerSerializer(answer).data,
                status=status.HTTP_201_CREATED)

    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


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
            tag = AddTagToQuestion(question, serializer.data['name'])
            return JsonResponse(
                quiz_serializers.TagSerializer(tag).data,
                status=status.HTTP_201_CREATED)

    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def SpecificTagTask(request, q_pk, t_pk):
    question = get_object_or_404(quiz_models.Question, pk=q_pk)
    tag = get_object_or_404(question.tag_set, pk=t_pk)

    if request.method == 'GET':
        serializer = quiz_serializers.TagSerializer(tag)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        question.tag_set.remove(tag)  # remove reference to tag, not delete tag
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
