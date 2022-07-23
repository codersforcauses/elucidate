from django.contrib import admin
from .models.quiz_models import Question, Tag, Answer
from .models.statistics_models import QuestionResponse


class AnswerInline(admin.TabularInline):
    model = Answer


class TagInline(admin.TabularInline):
    model = Tag.question.through
    verbose_name = "Tag"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
        TagInline,
    ]


admin.site.register(Tag)
admin.site.register(QuestionResponse)
