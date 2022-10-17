from django.urls import path
from users.views import (
    RegistrationView,
    SignInView,
    UserProfile,
    ContactUsAPIView,
    ChangeCurrentPasswordView,
    ForgotPassword,
    ProfilePhotoView
)
from django.conf.urls.static import static
from django.conf import settings

""" User Controls """
urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="register-new-user"),
    path("sign-in/", SignInView.as_view(), name="sign-in-user"),
    path("profile", UserProfile.as_view(), name="User profile"),
    path("contact-us", ContactUsAPIView.as_view(), name="contact-us"),
    path("change-password", ChangeCurrentPasswordView.as_view(), name="change-password"),
    path("forgot-password", ForgotPassword.as_view(), name="forgot-password"),
    path("", ProfilePhotoView.as_view(), name="profile-photo"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
