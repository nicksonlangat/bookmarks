from django.urls import path

from .views import UserRegisterApi, UserLoginApi, UserMeApi

urlpatterns = [
    path("users/me", UserMeApi.as_view(), name="users-me"),
    path("register/", UserRegisterApi.as_view(), name="register"),
    path("login/", UserLoginApi.as_view(), name="login"),
]
