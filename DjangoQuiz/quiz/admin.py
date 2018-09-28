from django.contrib import admin
from .models import *

# Register your models here.

class ChoiceInline(admin.TabularInline):   #TO add questions directly while creating a QUIZ
    model = QuestionTable
    extra = 1

class QuizTableAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Description',     {'fields': ['qno', 'qdesc']}),
    ]
    inlines = [ChoiceInline]           #TO add questions directly while creating a QUIZ               
    list_display = ('qno', 'qdesc')


class QuestionTableAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Description',     {'fields': ['qno', 'qid','qtext']}),
        ('Choices',         {'fields': ['opt1', 'opt2', 'opt3', 'opt4']}),
        ('Answer',          {'fields': ['ans']}),
    ]
    list_display = ('qno', 'qid', 'qtext', 'ans')
    list_filter = ['qno']



admin.site.register(QuizTable, QuizTableAdmin)
admin.site.register(QuestionTable, QuestionTableAdmin)