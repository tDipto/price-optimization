from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.SignupAPI.as_view(), name="UserSignupAPI"),
    path("signin/", views.SignInAPI.as_view(), name="SignInAPI"),
    path("user/<str:username>", views.ShowUserAPI.as_view(), name="ShowUserAPI"),
    path(
        "user/verify-otp/<str:username>/",
        views.OTPVerificationAPI.as_view(),
        name="OTPVerificationAPI",
    ),
]
