from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from .serializers import QuizCreationSerializer, QuizDetailSerializer
from .models import Quiz
from django.contrib.auth import get_user_model
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    message = "You must be the owner of this object."

    def has_object_permission(self, request, view, obj):
        print("inside here")
        return obj.creator == request.user.id


class QuizCreateListView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = QuizCreationSerializer
    queryset = Quiz.objects.all()

    def get(self, request):
        quizzes = Quiz.objects.all()
        serializer = self.serializer_class(instance=quizzes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        user = request.user
        if serializer.is_valid():
            serializer.save(creator=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuizDetailSerializer
    permission_classes = [IsAdminUser]
    queryset = Quiz.objects.all()

    def get(self, request, pk):
        quiz = Quiz.objects.get(id=pk)
        serializer = QuizDetailSerializer(instance=quiz)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        quiz = Quiz.objects.get(id=pk)
        serializer = QuizDetailSerializer(instance=quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        quiz = Quiz.objects.get(id=pk)
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserQuizListView(generics.ListAPIView, IsOwner):
    serializer_class = QuizDetailSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, user_pk):
        user = get_user_model().objects.get(id=user_pk)
        quizzes = Quiz.objects.filter(creator=user)
        serializer = self.serializer_class(instance=quizzes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserQuizDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuizDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = Quiz.objects.all()

    def get(self, request, user_pk, quiz_pk):
        user = get_user_model().objects.get(id=user_pk)
        quiz = Quiz.objects.all().filter(creator=user).get(id=quiz_pk)
        serializer = self.serializer_class(instance=quiz)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, user_pk, quiz_pk):
        user = get_user_model().objects.get(id=user_pk)
        quiz = Quiz.objects.all().filter(creator=user).get(id=quiz_pk)
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
