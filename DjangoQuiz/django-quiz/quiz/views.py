from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, View

from django.contrib.auth.models import User
from users.models import Score
from .models import QuizTable, QuestionTable

# Create your views here.

class HomePageView(ListView):
    model = QuizTable
    context_object_name = 'Quizes'
    template_name = 'quiz/HomePage.html'

    def get_context_data(self, **kwargs):
        scores, b = 0, Score.objects.filter(user = self.request.user)
        for i in b: scores += i.score 
        context = super().get_context_data(**kwargs)
        context['score'] = scores
        context['quizscore'] = b
        return context

class QuizPageView(View):
    def get(self, request, *args, **kwargs):
        Questions = QuestionTable.objects.filter(qno = self.kwargs['pk'])
        context = {'Questions':Questions,'pk': self.kwargs['pk']}
        return render(request, 'quiz/QuizPage.html', context)

    def post(self, request, *args, **kwargs):
        quiz_score = Score.objects.get(qno = self.kwargs['pk'], user = request.user)
        Questions = QuestionTable.objects.filter(qno = self.kwargs['pk'])
        points = 0
        for i in Questions:
            try:
                if(request.POST[i.qid] == i.ans):
                    points += 10
            except:
                pass
        if(quiz_score.score < points):
            quiz_score.score = points
            quiz_score.save()
        return render(request, 'quiz/ScorePage.html', {'points' : points})