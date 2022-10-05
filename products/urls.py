from django.urls import path
from products.views import (
    ProductAPIView,
    ProductDetailAPIView,
    ProductReviewAPIView,
    PublicProductAPIView,
    ProductToogleAPIView
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", ProductAPIView.as_view(), name="product api"),
    path("product-detail", ProductDetailAPIView.as_view(), name="product-review"),
    path("user-review", ProductReviewAPIView.as_view(), name="user-review"),
    path("get-all-products", PublicProductAPIView.as_view(), name="Public API"),
    path("toggle-product", ProductToogleAPIView.as_view(), name="toggle-product"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
