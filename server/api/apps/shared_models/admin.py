from django.contrib import admin
from .models.quiz_models import Question, Subject, Topic, Answer
from .models.statistics_models import QuizStatistics


class AnswerInline(admin.TabularInline):
    model = Answer


class SubjectInline(admin.TabularInline):
    model = Topic.question.through
    verbose_name = "Subject"


class TopicInline(admin.TabularInline):
    model = Subject
    verbose_name = "Topic"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
        SubjectInline,
    ]


admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(QuizStatistics)
