from .models import User
from django import forms
from django.conf import settings


# Form which contain Profile photo in usr-account.html
class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image']
