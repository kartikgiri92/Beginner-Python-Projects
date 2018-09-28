from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
	path('loginpage/', views.LoginPageView.as_view(), name = 'loginpage'),
	path('userregister/', views.UserRegisterView.as_view(), name = 'userregister'),
	path('profile/', views.ProfileView.as_view(), name = 'profile'),
	path('logout/', views.LogoutView.as_view(), name = 'logout'),
]