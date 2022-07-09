from rest_framework import routers, serializers, viewsets
from .models import Quiz_Details

class Quiz_DetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz_Details
        fields = ['id', 'name', 'time_limit', 'date_created', 'number_of_questions']

#{
#    "name": "quiztest",
#    "time_limit": 1000,
#    "date_created": "2012-04-23T18:25:43.511Z",
#    "creator": "me",
#    "tags": [ "test1" ],
#    "objectives": [ "test2" ],
#    "number_of_questions": 3
#}