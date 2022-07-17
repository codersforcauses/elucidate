from django.contrib import admin
from .models import Quiz


# Register your models here.
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ["title", "question", "category", "creator", "created_at"]
    list_filter = ["category", "created_at"]
