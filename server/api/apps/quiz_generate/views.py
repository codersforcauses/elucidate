import random

from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from api.apps.shared_models.models.quiz_models import Question, Subject, Topic
from api.apps.shared_models.serializers import question_serializers

# from api.apps.quizzes import

from .serializers import GenerateQuizRequestSerializer
from api.apps.quizzes.models import Quiz
from django.db.models import Q


class GenerateQuizView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GenerateQuizRequestSerializer
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
            questions = questions.filter(topics__in=serializer.data["topics"]).distinct()
            print(questions)
            if not serializer.data["question_types"]["multiple_choice"]:
                questions = questions.filter(~Q(question_type="MC"))

            if not serializer.data["question_types"]["numeric"]:
                questions = questions.filter(~Q(question_type="NA"))

            if not serializer.data["question_types"]["short_answer"]:
                questions = questions.filter(~Q(question_type="SA"))

            question_count = serializer.data["question_count"]
            if question_count < 1 or questions.count() < 1:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            # make sure question_count is not larger than pk_list
            if question_count > questions.count():
                question_count = questions.count()

            question_pks = [question.pk for question in questions]
            random_pks = random.sample(question_pks, question_count)
            quiz = Quiz.objects.create()
            quiz.topics.set(serializer.data["topics"])
            quiz.questions.set(random_pks)
            quiz.user = request.user
            quiz.save()
            return Response({"quiz_id": quiz.pk})


class SubjectExistsView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = question_serializers.SubjectSerializer
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
    serializer_class = question_serializers.TopicSerializer
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
