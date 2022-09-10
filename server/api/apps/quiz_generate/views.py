from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from . import serializers
from rest_framework import status
from api.apps.shared_models.models.quiz_models import Question, Topic, Subject
from api.apps.shared_models.serializers import quiz_serializers
from rest_framework.response import Response
import random


class GenerateQuizView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GenerateQuizRequestSerializer
    queryset = Question.objects.all()

    """
    POST request to return random questions based on request parameters.
    """

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # filter questions by verification, subject and topics
            questions = self.get_queryset()
            questions = questions.filter(is_verified=True)
            questions = questions.filter(subject=serializer.data["subject"])
            for topic in serializer.data["topics"]:
                questions = questions.filter(topics=topic)

            # create a list of just the question PKs
            pk_list = []
            for question in questions:
                pk_list.append(question.pk)

            question_count = serializer.data["question_count"]
            if question_count < 1:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            # make sure question_count is not larger than pk_list
            if question_count > questions.count():
                question_count = questions.count()
            return Response(
                {"pk_array": random.sample(pk_list, question_count)}
            )


class SubjectExistsView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = quiz_serializers.SubjectSerializer
    queryset = Subject.objects.all()

    """
    POST request to check if a subject exists in the database.
    If it does exist, return the subject's PK.
    """

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            subject = get_object_or_404(
                self.get_queryset(), name=serializer.data["name"]
            )
            return Response({"pk": subject.pk})


class TopicExistsView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = quiz_serializers.TopicSerializer
    queryset = Topic.objects.all()

    """
    POST request to check if a topic exists in the database.
    If it does exist, check that it is related to the subject and
    return the topic's PK.
    """

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            topic = get_object_or_404(
                self.get_queryset(),
                name=serializer.data["name"],
                subject=serializer.data["subject"],
            )
            return Response({"pk": topic.pk})
