from django import forms
from django.contrib import admin

from .models import Quiz


# Register your models here.


# class QuizAdmin(admin.ModelAdmin):
#     list_display = ["created_at"]
#     # list_filter = ["category", "created_at"]


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ["questions", "topic"]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    # readonly_fields = ["date_created"]
    form = QuizForm

    def get_object(self, request, object_id, s):
        self.obj = super(QuizAdmin, self).get_object(request, object_id)
        return self.obj
