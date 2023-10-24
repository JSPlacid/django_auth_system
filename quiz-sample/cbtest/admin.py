from django.contrib import admin
from .models import Quiz, Question, Option

# Register your models here.


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    """class for question model"""
    list_display = ('title', 'description', 'duration_minutes')


class OptionInline(admin.StackedInline):
    model = Option
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """class for question model"""
    list_display = ['text']

    inlines = [OptionInline]


@admin.register(Option)
class AnswerAdmin(admin.ModelAdmin):
    """class for answer model"""
    list_display = ('text', 'question', 'is_correct')

    fieldsets = (
        (None, {
            'fields': ('question', 'text',)
        }),
    )
