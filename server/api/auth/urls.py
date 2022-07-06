from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('token', obtain_jwt_token, name='get-jwt-token'),
    path('token/refresh', refresh_jwt_token, name='refresh-jwt-token')
]
