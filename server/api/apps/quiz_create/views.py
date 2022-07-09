from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .serializers import Quiz_DetailsSerializer
from .models import Quiz_Details

from django.views.decorators.csrf import csrf_exempt  # will change this later

@csrf_exempt
def QuizTask(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = Quiz_DetailsSerializer(data=data)
        if(serializer.is_valid(raise_exception=True)):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    else:
        return HttpResponse(status=400)      # bad request

@csrf_exempt
def SpecificQuizTask(request, pk):
    Quiz = get_object_or_404(Quiz_Details, pk=pk)
    
    if(request.method == 'GET'):
        serializer = Quiz_DetailsSerializer(Quiz)
        return JsonResponse(serializer.data)
    else:
        return HttpResponse(status=400)      # bad request
