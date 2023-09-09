from django.urls import path

from .views import (
    UserRegisterApi, UserLoginApi, 
    UserMeApi, UserPasswordResetApi, 
    UserPasswordTokenCheckApi, UserSetNewPasswordApi
)

urlpatterns = [
    path("users/me", UserMeApi.as_view(), name="users-me"),
    path("register/", UserRegisterApi.as_view(), name="register"),
    path("login/", UserLoginApi.as_view(), name="login"),
    path("password/reset/", UserPasswordResetApi.as_view(), name="password-reset"),
    path('password-reset/<uidb64>/<token>/', UserPasswordTokenCheckApi.as_view(),name='token-check'),
    path('new/password/', UserSetNewPasswordApi.as_view(),name='new-password'),
]
