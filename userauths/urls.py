import imp
from django.urls import path
from userauths import *
from userauths.views import RegisterView, loginView, logoutView

urlpatterns = [
    path("sign-up/", RegisterView, name="sign-up"),
    path("sign-in/", loginView, name="sign-in"),
    path("sign-out/", logoutView, name="sign-out"),
]