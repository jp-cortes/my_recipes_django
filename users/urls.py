from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RegisterView

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(template_name="users/login.html"),
        name="login"
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name="users/log_out.html"),
        name="logout"
    ),
    path(
        'signup/',
        RegisterView.as_view(template_name="users/register.html"),
        name="register"
    ),
]