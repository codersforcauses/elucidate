from django.urls import path
from api.apps.users.view import UserAPIView


urlpatterns = [
    # User endpoints
    path("", UserAPIView.as_view(), name="user")
]
