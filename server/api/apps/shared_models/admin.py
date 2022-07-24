from django.contrib import admin
from .models.quiz_models import Question, Tag, Answer
from .models.statistics_models import QuestionResponse, UserStatistics, QuizStatistics, QuizTag


class AnswerInline(admin.TabularInline):
    model = Answer


class TagInline(admin.TabularInline):
    model = Tag.question.through
    verbose_name = "Tag"


class QuizTagInline(admin.TabularInline):
    model = QuizTag.quiz_statistics.through
    verbose_name = "Quiz Tag"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
        TagInline,
    ]


@admin.register(QuizStatistics)
class QuizStatisticsAdmin(admin.ModelAdmin):
    inlines = [
        QuizTagInline,
    ]

@admin.register(UserStatistics)
class UserStatisticsAdmin(admin.ModelAdmin):
    list_display = ("user", "quizzes_completed", "average_score", "questions_created")
    readonly_fields = ["questions_created", "average_score"]


admin.site.register(Tag)
admin.site.register(QuestionResponse)
