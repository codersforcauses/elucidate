from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework import status


class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
