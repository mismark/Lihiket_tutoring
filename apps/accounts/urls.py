from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views

app_name = "accounts"

urlpatterns = [
    
    # homepage
    path("", views.home, name="home"),

    # Authentication
    path("register/", views.register_view, name="register"),
    
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Profile
    path("profile/", views.profile_view, name="profile"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),

    # Password Reset
    path(
        "forgot-password/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/forgot_password.html",
            success_url=reverse_lazy("accounts:password_reset_done"),
        ),
        name="forgot_password",
    ),

    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html",
        ),
        name="password_reset_done",
    ),

    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            success_url=reverse_lazy("accounts:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),

    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
]