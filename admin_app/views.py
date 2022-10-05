import logging
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        )

from baselayer.baseapiviews import BaseAPIView
from baselayer.baseauthentication import JWTAuthentication, JWTAdminAuthentication
from products.serializers import ProductSerializer, ProductReviewSerializer
from utils.mock_responses import ResponseMessages
from reviewer import settings
from products.models import (
    Product, ProductApprovalStatusChoices, ProductReview, ProductReviewApprovalStatusChoices
)
from utils.baseutils import (
    get_first_error_message_from_serializer_errors,
)
logger = logging.getLogger(settings.LOGGER_NAME_PREFIX + __name__)


class ProductAPIView(BaseAPIView):
    """ Product CRUD APIView """

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAdminAuthentication]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def patch(self, request, *args, **kwargs):
        approval_status = request.data.get("approval_status", None)
        product_id = request.data.get("product_id", None)

        if not approval_status and not product_id:
            return self.send_bad_request_response(
                message=ResponseMessages.PRODUCT_ID_AND_APPROVAL_STATUS_IS_REQUIRED.value
            )
        if int(approval_status) == 2:
            Product.objects.filter(id=product_id).update(approval_status=ProductApprovalStatusChoices.APPROVED)
        elif int(approval_status) == 3:
            Product.objects.filter(id=product_id).update(approval_status=ProductApprovalStatusChoices.REJECTED)

        return self.send_success_response(
            message=ResponseMessages.SUCCESS.value
        )


    def get(self, request, *args, **kwargs):
        query = dict()
        if "id" in request.query_params:
            query.update({"id": request.query_params["id"]})

        if "category" in request.query_params:
            query.update({"category": request.query_params["category"]})

        if "title" in request.query_params:
            query.update({"title__icontains": request.query_params["title"]})

        instances = self.queryset.filter(**query)

        return self.send_success_response(
            payload=self.serializer_class(instances, many=True).data,
            message=ResponseMessages.SUCCESS.value
        )


class ProductReviewAPIView(BaseAPIView):
    """ Product Review APIView """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAdminAuthentication]
    serializer_class = ProductReviewSerializer
    queryset = ProductReview.objects.all()

    def get(self, request, *args, **kwargs):
        instances = self.queryset.filter(approval_status=ProductReviewApprovalStatusChoices.PENDING)
        return self.send_success_response(
            payload=self.serializer_class(instances, many=True).data,
            message=ResponseMessages.SUCCESS.value
        )

    def patch(self, request, *args, **kwargs):
        id = request.query_params.get("id", None)
        status = request.query_params.get("status", None)
        all = request.query_params.get("all", None)
        if all is not None:
            if str(status) == "1":
                self.queryset.filter(approval_status=ProductReviewApprovalStatusChoices.PENDING).update(approval_status=ProductReviewApprovalStatusChoices.APPROVED)
            if str(status) == "2":
                self.queryset.filter(approval_status=ProductReviewApprovalStatusChoices.PENDING).update(approval_status=ProductReviewApprovalStatusChoices.REJECTED)
        if id is not None:
            if str(status) == "1":
                self.queryset.filter(id=id).update(approval_status=ProductReviewApprovalStatusChoices.APPROVED)
            if str(status) == "2":
                self.queryset.filter(id=id).update(approval_status=ProductReviewApprovalStatusChoices.REJECTED)
        return self.send_success_response("Success")
