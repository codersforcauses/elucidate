from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet, UserStatistics

router = routers.DefaultRouter()
router.register(r"", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("<int:pk>", views.UserStatistics.as_view(), name = 'user-statistics' )
]
