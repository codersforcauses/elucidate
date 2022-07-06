from django.urls import path
from api.users.view import UserAPIView


urlpatterns = [
    # User endpoints
    path('', UserAPIView.as_view(), name='user')
]
