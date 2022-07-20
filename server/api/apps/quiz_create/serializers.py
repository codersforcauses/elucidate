from rest_framework import serializers
from api.apps.shared_models.models import defines

QuestionTypes = [
    ("MC", "Multiple Choice"),
    ("NA", "Numerical Answer"),
    ("SA", "Short Answer")
]


class QuestionInfoSerializer(serializers.Serializer):
    text = serializers.CharField(allow_blank=True)
    date_created = serializers.DateTimeField()
    question_type = serializers.ChoiceField(choices=QuestionTypes)
    answers = serializers.ListField(
        child=(
            serializers.ListField(  # will vailidate types in views
                allow_empty=False,
                min_length=2,
                max_length=2)
            ),
        required=False,
        allow_empty=True
        )
    tags = serializers.ListField(
        child=serializers.CharField(max_length=defines.TAG_NAME_MAXLEN)
        )
    # no idea how user verification is gonna work
    # creator = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    # )
