from django.db import models
from django.core.validators import MinLengthValidator
from baselayer.basemodels import LogsMixin
from users.models import User
from django.utils import timezone


# Status Model - PRODUCT
class ProductApprovalStatusChoices(models.TextChoices):
    PENDING = 1, "Pending"   # Product is hidden from being displayed to users in Carousel and only displayed for Admin in products.html datatable
    APPROVED = 2, "Approved" # Product is displayed in Carousel and also displayed in products.html
    REJECTED = 3, "Rejected" # Product is deleted along with product reviews associated with that specific product
    
# Status Model - PRODUCT REVIEW
class ProductReviewApprovalStatusChoices(models.TextChoices):
    PENDING = 0, "Pending" # Product Review is displayed only in approve-reviews.html - awaiting decision to be approved or rejected.
    APPROVED = 1, "Approved" # Product Review is approved and displayed in #users-reviews-box
    REJECTED = 2, "Rejected" # Product Review is deleted

# Product Model
class Product(LogsMixin):
    """ Product Model """
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2) # for future implementation
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

# Product Review Model
class ProductReview(LogsMixin):
    """ Product Review Model """
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=800,
        validators=[
            MinLengthValidator(
                10, 'Your comment must be longer than that!')
        ]
    )
    rating = models.FloatField(default=1.0)
    category = models.CharField(max_length=150)
    session = models.CharField(max_length=150)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews")
    review_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews")
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
