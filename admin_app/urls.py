from django.urls import path
from admin_app.views import (
    ProductAPIView,
    ProductReviewAPIView
)

urlpatterns = [
    path("products", ProductAPIView.as_view(), name="product control by admin"),
    path("reviews", ProductReviewAPIView.as_view(), name="product review control by admin"),
]
