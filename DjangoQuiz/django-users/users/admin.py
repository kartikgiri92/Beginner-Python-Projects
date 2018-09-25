from django.contrib import admin
from .models import *

# Register your models here.

class ScoreTableAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('Description',     {'fields': ['qno', 'qid','qtext']}),
    #     ('Choices',         {'fields': ['opt1', 'opt2', 'opt3', 'opt4']}),
    #     ('Answer',          {'fields': ['ans']}),
    # ]
    list_display = ('user', 'qno', 'score')

admin.site.register(Score, ScoreTableAdmin)
