from django import forms
from django.contrib import admin

from .models import Quiz, QuizQuestion


# Register your models here.


# class QuizAdmin(admin.ModelAdmin):
#     list_display = ["created_at"]
#     # list_filter = ["category", "created_at"]


class QuizQuestionInline(admin.TabularInline):
    model = QuizQuestion
    extra = 1


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ["questions", "topics"]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    # readonly_fields = ["date_created"]
    form = QuizForm
    inlines = [QuizQuestionInline]

    def get_object(self, request, object_id, s):
        self.obj = super(QuizAdmin, self).get_object(request, object_id)
        return self.obj
