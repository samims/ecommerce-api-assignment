from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignupView

app_name = 'users'

urlpatterns = [
    path('signup/', SignupView.as_view(template_name='users/signup.html')),
    path("login/", LoginView.as_view(template_name='users/login.html')),
    path("logout/", LogoutView.as_view()),
]
