from django import forms
from django.contrib import admin
from django.forms import ValidationError

from .models.quiz_models import Answer, Question, Subject, Topic
from .models.statistics_models import (QuestionResponse, QuestionStatistics,
                                       QuizStatistics, TopicStatistics,
                                       UserStatistics)


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["text", "question_type", "marks", "subject", "topics"]

    def clean(self):
        subject = self.cleaned_data.get("subject")
        topics = self.cleaned_data.get("topics")
        if subject and topics:
            for topic in topics:
                if topic.subject != subject:
                    raise ValidationError(
                        f'Invalid topic "{topic}": this topic belongs to the'
                        f' subject "{topic.subject}" whereas the question'
                        f' belongs to the subject "{subject}".'
                    )
        return self.cleaned_data


class QuestionResponseForm(forms.ModelForm):
    class Meta:
        model = QuestionResponse
        fields = ["user", "question", "selected_answer"]

    def clean(self):
        selected_answer = self.cleaned_data.get("selected_answer")
        answers = Answer.objects.filter(
            question=self.cleaned_data.get("question")
        )
        if selected_answer and answers:
            if selected_answer not in answers:
                raise ValidationError(
                    f'Invalid selected answer "{selected_answer}": this answer'
                    " is not an option for the question."
                )
        return self.cleaned_data


class QuizStatisticsForm(forms.ModelForm):
    class Meta:
        model = QuizStatistics
        fields = [
            "user",
            "quiz_title",
            "subject",
            "topics",
            "date_taken",
            "score",
        ]

    def clean(self):
        subject = self.cleaned_data.get("subject")
        topics = self.cleaned_data.get("topics")
        if subject and topics:
            for topic in topics:
                if topic.subject != subject:
                    raise ValidationError(
                        f'Invalid topic "{topic}": this topic belongs to the'
                        f' subject "{topic.subject}" whereas the question'
                        f' belongs to the subject "{subject}".'
                    )
        return self.cleaned_data


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]
    readonly_fields = ["date_created"]
    form = QuestionForm

    def get_object(self, request, object_id, s):
        self.obj = super(QuestionAdmin, self).get_object(request, object_id)
        return self.obj

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "topics":
            kwargs["queryset"] = Topic.objects.filter(subject=self.obj.subject)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(QuestionResponse)
class QuestionResponseAdmin(admin.ModelAdmin):
    readonly_fields = ["date_submitted"]
    form = QuestionResponseForm

    def get_object(self, request, object_id, s):
        self.obj = super(QuestionResponseAdmin, self).get_object(
            request, object_id
        )
        return self.obj

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "selected_answer":
            kwargs["queryset"] = Answer.objects.filter(
                question=self.obj.question
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(QuizStatistics)
class QuizStatisticsAdmin(admin.ModelAdmin):
    form = QuizStatisticsForm

    def get_object(self, request, object_id, s):
        self.obj = super(QuizStatisticsAdmin, self).get_object(
            request, object_id
        )
        return self.obj

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "topics":
            kwargs["queryset"] = Topic.objects.filter(subject=self.obj.subject)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(UserStatistics)
class UserStatisticsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "quizzes_completed",
        "average_score",
        "questions_created",
    )
    readonly_fields = [
        "quizzes_completed",
        "questions_created",
        "average_score",
    ]


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
