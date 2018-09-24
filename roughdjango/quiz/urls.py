from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
	path('', views.HomePageView.as_view(), name = 'HomePage'),
	path('<int:pk>/', views.QuizPageView.as_view(), name = 'QuizPage'),
]