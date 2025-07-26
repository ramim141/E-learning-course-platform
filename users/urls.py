# users/urls.py

from django.urls import path
from .views import (
    UserRegistrationView,
    EmailVerificationView,
    UserLoginView,
    UserProfileView,
    RequestPasswordResetView,
    ConfirmPasswordResetView,
)

urlpatterns = [
    # Auth
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('verify-email/<uidb64>/<token>/', EmailVerificationView.as_view(), name='email-verify'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    
    # Profile
    path('profile/', UserProfileView.as_view(), name='user-profile'),

    # Password Reset
    path('password-reset/request/', RequestPasswordResetView.as_view(), name='request-password-reset'),
    path('password-reset/confirm/<uidb64>/<token>/', ConfirmPasswordResetView.as_view(), name='confirm-password-reset'),
]