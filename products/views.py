import logging
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        )

from baselayer.baseapiviews import BaseAPIView
from baselayer.baseauthentication import JWTAuthentication
from products.serializers import ProductSerializer, ProductDetailSerializer, ProductReviewSerializer
from utils.mock_responses import ResponseMessages
from reviewer import settings
from products.models import (
    Product, ProductApprovalStatusChoices,
)
from utils.baseutils import (
    get_first_error_message_from_serializer_errors,
)
logger = logging.getLogger(settings.LOGGER_NAME_PREFIX + __name__)


class PublicProductAPIView(BaseAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        query = {}
        if "id" in request.query_params:
            query.update({"id": request.query_params["id"]})

        if "category" in request.query_params:
            query.update({"category": request.query_params["category"]})

        if "title" in request.query_params:
            query.update({"title__icontains": request.query_params["title"]})

        instances = self.queryset.filter(**query).exclude(is_hide=True)

        return self.send_success_response(
            payload=self.serializer_class(instances, many=True).data,
            message=ResponseMessages.SUCCESS.value
        )

class ProductAPIView(BaseAPIView):
    """Product CRUD APIView"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        if not serializer.is_valid():
            logger.error(serializer.errors)
            return self.send_bad_request_response(
                message=get_first_error_message_from_serializer_errors(
                    serialized_errors=serializer.errors,
                    default_message=ResponseMessages.SOMETHING_MISSING_IN_REQUEST,
                )
            )
        instance = serializer.save()
        return self.send_success_response(
            payload=self.serializer_class(instance).data,
            message=ResponseMessages.PRODUCT_CREATED_SUCCESSFULLY.value
        )

    def patch(self, request, *args, **kwargs):
        if "id" not in request.query_params:
            return self.send_bad_request_response(
                message=ResponseMessages.PRODUCT_ID_REQUIRED.value
            )
        instance = self.queryset.filter(id=request.query_params["id"]).first()
        if instance:
            instance.title = request.data.get("title") if request.data.get("title") not in [None, "undefined"] else instance.title
            instance.description = request.data.get("description") if request.data.get("description") not in [None, "undefined"] else instance.description
            instance.category = request.data.get("category") if request.data.get("category") not in [None, "undefined"] else instance.category
            instance.image = request.data.get("image") if request.data.get("image") not in [None, "undefined"] else instance.image
            instance.save()
        return self.send_success_response(
            payload=dict(),
            message=ResponseMessages.PRODUCT_UPDATED_SUCCESSFULLY.value
        )

    def delete(self, request, *args, **kwargs):
        if "id" not in request.query_params:
            return self.send_bad_request_response(
                message=ResponseMessages.PRODUCT_ID_REQUIRED.value
            )
        self.queryset.filter(id=request.query_params["id"]).delete()
        return self.send_success_response(
            message=ResponseMessages.PRODUCT_DELETED_SUCCESSFULLY.value
        )

    def get(self, request, *args, **kwargs):
        instance = self.queryset.all()
        return self.send_success_response(
            payload=self.serializer_class(instance, context={"request": request}, many=True).data,
            message=ResponseMessages.SUCCESS.value
        )


class ProductToogleAPIView(BaseAPIView):
    """Product toogle APIView"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def patch(self, request, *args, **kwargs):
        if "id" not in request.query_params:
            return self.send_bad_request_response(
                message=ResponseMessages.PRODUCT_ID_REQUIRED.value
            )
        instance = self.queryset.filter(id=request.query_params["id"]).first()
        if instance:
            if instance.is_hide == False:
                instance.is_hide = True
            else:
                instance.is_hide = False
            instance.save()
        return self.send_success_response(
            payload=dict(),
            message=ResponseMessages.PRODUCT_TOGGLED_SUCCESSFULLY.value
        )

class ProductDetailAPIView(BaseAPIView):

    permission_classes = [AllowAny]
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        if "id" not in request.query_params:
            return self.send_bad_request_response(
                message=ResponseMessages.PRODUCT_ID_REQUIRED.value
            )
        instance = self.queryset.filter(id=request.query_params["id"]).first()
        if not instance:
            return self.send_bad_request_response(
                message=ResponseMessages.PRODUCT_NOT_FOUND.value
            )
        return self.send_success_response(
            payload=self.serializer_class(instance).data,
            message=ResponseMessages.SUCCESS.value
        )


class ProductReviewAPIView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ProductReviewSerializer
    queryset = Product.objects.all()

    def post(self, request, *args, **kwargs):
        if "product" not in request.data:
            return self.send_bad_request_response(
                message=ResponseMessages.PRODUCT_ID_REQUIRED.value
            )
        instance = self.queryset.filter(id=request.data["product"]).first()
        if not instance:
            return self.send_bad_request_response(
                message=ResponseMessages.PRODUCT_NOT_FOUND.value
            )
        serializer = self.serializer_class(data=request.data, context={"request": request})
        if not serializer.is_valid():
            logger.error(serializer.errors)
            return self.send_bad_request_response(
                message=get_first_error_message_from_serializer_errors(
                    serialized_errors=serializer.errors,
                    default_message=ResponseMessages.SOMETHING_MISSING_IN_REQUEST,
                )
            )
        instance = serializer.save()
        return self.send_success_response(
            payload=self.serializer_class(instance).data,
            message=ResponseMessages.PRODUCT_REVIEW_CREATED_SUCCESSFULLY.value
        )
