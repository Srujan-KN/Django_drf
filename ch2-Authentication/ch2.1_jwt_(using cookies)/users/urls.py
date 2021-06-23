from django.urls import path
from .views import RegisterView, LoginView,UserView,LogoutView
from helloworld.views import TestView
urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('user', UserView.as_view()),
    path('hello',TestView.as_view()),
    path('logout',LogoutView.as_view()),
]