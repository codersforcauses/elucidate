from django.urls import path

from . import views

# will change this later
urlpatterns = [
    path('', views.index, name='index'),
]