from django.shortcuts import render
from django.http import HttpResponse


# will change this later
def index(request):
    return HttpResponse("Hello, world.")