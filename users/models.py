from django.db import models
from baselayer.basemodels import LogsMixin
from django.contrib.auth.models import AbstractUser
from baselayer.baseauthentication import generate_access_token
from django.utils import timezone

# Choice classes
# User and Admin authentication
class UserTypeChoices(models.TextChoices):
    ADMIN = 1, "Admin"
    USER = 3, "User"


# User Account Model
class User(LogsMixin, AbstractUser):
    user_type = models.CharField(choices=UserTypeChoices.choices, null=True,
                                 blank=True, max_length=25, default=UserTypeChoices.USER)
    location = models.CharField(max_length=100, null=True, blank=True)
    skill_level = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to="users/", null=True, blank=True)

    reset_password_token = models.CharField(
        max_length=100, null=True, blank=True)

    def get_access_token(self):
        return generate_access_token(self)

# ContactUs Form Model
class ContactUs(LogsMixin, models.Model):
    
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=1000, null=True, blank=True)

    def get_date(self):
        now = timezone.now()
        days_ago = now - self.created_at
        if days_ago.days == 0:
            return "Today"
        elif days_ago.days == 1:
            return "Yesterday"
        else:
            return f"{days_ago.days} days ago"

