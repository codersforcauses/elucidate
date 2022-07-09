from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from api.apps.users.serializers import UserSerializer


class UserAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    permissions_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
