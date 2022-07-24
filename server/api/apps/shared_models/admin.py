from django.contrib import admin
from .models.quiz_models import Question, Subject, Topic, Answer, QuestionForm
from .models.statistics_models import QuestionResponse, UserStatistics, QuizStatistics, QuizTag, QuestionStatistics, TopicStatistics


class AnswerInline(admin.TabularInline):
    model = Answer


class QuizTagInline(admin.TabularInline):
    model = QuizTag.quiz_statistics.through
    verbose_name = "Quiz Tag"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]
    form = QuestionForm

    def get_object(self, request, object_id, s):
        self.obj = super(QuestionAdmin, self).get_object(request, object_id)
        return self.obj

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "topics":
            kwargs["queryset"] = Topic.objects.filter(subject=self.obj.subject)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(QuizStatistics)
class QuizStatisticsAdmin(admin.ModelAdmin):
    inlines = [
        QuizTagInline,
    ]


@admin.register(UserStatistics)
class UserStatisticsAdmin(admin.ModelAdmin):
    list_display = ("user", "quizzes_completed", "average_score", "questions_created")
    readonly_fields = ["questions_created", "average_score"]


@admin.register(QuestionStatistics)
class QuestionStatisticsAdmin(admin.ModelAdmin):
    list_display = ("question", "number_attempts", "average_score")
    readonly_fields = ["number_attempts", "average_score"]


@admin.register(TopicStatistics)
class TopicStatisticsAdmin(admin.ModelAdmin):
    list_display = ("topic", "average_score")
    readonly_fields = ["average_score"]


admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(QuestionResponse)
