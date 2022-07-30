from django.urls import path
from . import views

app_name = "user_statistics"
urlpatterns = [
    path(
        "user/<int:user_pk>/",
        views.UserStatisticsDetailView.as_view(),
        name="stats",
    ),
]
