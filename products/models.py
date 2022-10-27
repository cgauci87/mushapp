from django.db import models
from baselayer.basemodels import LogsMixin
from users.models import User
from django.utils import timezone

class ProductApprovalStatusChoices(models.TextChoices):
    PENDING = 1, "Pending"
    APPROVED = 2, "Approved"
    REJECTED = 3, "Rejected"

class ProductReviewApprovalStatusChoices(models.TextChoices):
    PENDING = 0, "Pending"
    APPROVED = 1, "Approved"
    REJECTED = 2, "Rejected"


class Product(LogsMixin):
    """ Product Model """
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=150)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_hide = models.BooleanField(default=False)
    approval_status = models.CharField(
        choices=ProductApprovalStatusChoices.choices,
        null=True,
        blank=True,
        max_length=25,
        default=ProductApprovalStatusChoices.PENDING
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="products"
    )


class ProductReview(LogsMixin):
    """ Product Review Model """
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=800)
    rating = models.FloatField(default=0.0)
    category = models.CharField(max_length=150)
    session = models.CharField(max_length=150)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    review_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    approval_status = models.CharField(
        choices=ProductReviewApprovalStatusChoices.choices,
        null=True,
        blank=True,
        max_length=25,
        default=ProductReviewApprovalStatusChoices.PENDING
    )

    def get_date(self):
        now = timezone.now()
        days_ago = now - self.created_at
        if days_ago.days == 0:
            return "Today"
        elif days_ago.days == 1:
            return "Yesterday"
        else:
            return f"{days_ago.days} days ago"
