from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, View
from django.views.generic.edit import FormView
from .models import Score
from django.contrib.auth.models import User
from .forms import LoginPageForm, UserRegisterForm
# Create your views here.

class LoginPageView(View):
    def post(self, request):
        form = LoginPageForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return(HttpResponseRedirect(reverse('quiz:HomePage')))
        return render(request, 'users/LoginPage.html', {'form': form})
    def get(self, request):
        if(not(request.user.is_authenticated)):
            form = LoginPageForm()
            return render(request, 'users/LoginPage.html', {'form': form})
        else:
            return(HttpResponseRedirect(reverse('quiz:HomePage')))

class LogoutView(View):
    def get(self, request):
        logout(request)
        return(HttpResponseRedirect(reverse('users:loginpage')))

class ProfileView(ListView):
    model = User
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        scores, b = 0, Score.objects.filter(user = self.request.user)
        for i in b: scores += i.score 
        context = super().get_context_data(**kwargs)
        context['score'] = scores
        return context

class UserRegisterView(FormView):
    template_name = 'users/UserRegister.html'
    form_class = UserRegisterForm
    def form_valid(self, form):
        form.save()
        return(HttpResponseRedirect(reverse('users:loginpage')))