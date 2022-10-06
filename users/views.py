import logging
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        )

from baselayer.baseapiviews import BaseAPIView
from baselayer.baseauthentication import JWTAuthentication
from utils.mock_responses import ResponseMessages
from reviewer import settings
from users.models import (
    User,
    ContactUs,
)
from users.serializers import (
    RegistrationSerializer,
)
from utils.baseutils import (
    get_first_error_message_from_serializer_errors,
)
from reviewer.settings import (
    DEFAULT_FROM_EMAIL, EMAIL_HOST_USER
)
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

logger = logging.getLogger(settings.LOGGER_NAME_PREFIX + __name__)

# try:
#     from django.contrib.auth.hashers import make_password
#     from users.models import User, UserTypeChoices
#     User.objects.update_or_create(
#         email="mushcommunityblog@gmail.com",
#         username="superadmin",
#         defaults={
#             "user_type": UserTypeChoices.ADMIN,
#             "password": make_password("$etanewPassw0rd")
#         }
#     )
# except Exception as err:
#     print("Error while creating superadmin", err)


class RegistrationView(BaseAPIView):
    """User registration APIView"""

    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        print(request)
        serializer_registration = self.serializer_class(data=request.data)
        if not serializer_registration.is_valid():
            logger.error(serializer_registration.errors)
            return self.send_bad_request_response(
                message=get_first_error_message_from_serializer_errors(
                    serialized_errors=serializer_registration.errors,
                    default_message=ResponseMessages.SOMETHING_MISSING_IN_REQUEST,
                )
            )
        user = serializer_registration.save()
        print(user)
        return self.send_success_response(
            payload=self.serializer_class(user).data,
            message=ResponseMessages.ACCOUNT_CREATED
        )


class SignInView(BaseAPIView):
    """User Sign in APIView"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # User.objects.filter(phone_number="+55355524558").delete()
        """Login end user

        Example:
            Request Body:
                API URL: http://users/sign-in/
                {
                    "email": "abc@gmail.com",
                    "password": "pass@word"
                }
            Response Body:
                {
                    "success": true,
                    "payload": {
                        "token": "jwt-token"
                    },
                    "message": "Logged in successfully."
                }
        """

        username = request.data.get("username", None)
        password = request.data.get("password", None)

        if not username:
            return self.send_bad_request_response(
                message=ResponseMessages.SOMETHING_MISSING_IN_REQUEST
            )

        if not password:
            return self.send_bad_request_response(
                message=ResponseMessages.SOMETHING_MISSING_IN_REQUEST
            )

        user = User.objects.filter(
            username=request.data.get("username")).first()
        if not user:
            user = User.objects.filter(
                email=request.data.get("username")).first()

        if not user:
            return self.send_response(
                success=False,
                message=ResponseMessages.INVALID_EMAIL,
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        if not user.check_password(request.data.get("password")):
            return self.send_response(
                success=False,
                message=ResponseMessages.INVALID_PASSWORD,
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        token = user.get_access_token()
        return self.send_success_response(
            message=ResponseMessages.LOGGED_IN_SUCCESSFULLY, payload={"token": token,
                                                                      "username": user.username,
                                                                      "email": user.email,
                                                                      "user_type": user.user_type
                                                                      })


class UserProfile(BaseAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        data = {
            "username": request.user.username,
            "email": request.user.email,
            "name": request.user.first_name + request.user.last_name,
            "location": request.user.location,
            "skill_level": request.user.skill_level,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "profile_image": str(request.user.profile_image) if request.user.profile_image else ""
        }
        return self.send_success_response(message="Success", payload=data)

    def patch(self, request, *args, **kwargs):
        user = request.user
        print(request.data.get("profile_image"))
        print(type(request.data.get("profile_image")))
        user.first_name = request.data.get("first_name") if request.data.get(
            "first_name") else user.first_name
        user.last_name = request.data.get("last_name") if request.data.get(
            "last_name") else user.last_name
        user.email = request.data.get("email") if request.data.get(
            "email") else user.email
        user.skill_level = request.data.get("skill_level") if request.data.get(
            "skill_level") else user.skill_level
        user.profile_image = request.data.get("profile_image") if request.data.get(
            "profile_image") else user.profile_image
        user.location = request.data.get("location") if request.data.get(
            "location") else user.location
        user.save()
        return self.send_success_response(message="Success")


class ContactUsAPIView(BaseAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        ContactUs.objects.create(
            first_name=request.data.get("first_name"),
            last_name=request.data.get("last_name"),
            email=request.data.get("email"),
            message=request.data.get("message"),
            created_at=request.data.get("created_at"),
        )
        return self.send_success_response(message="Success")

    def get(self, request, *args, **kwargs):
        contact_us = ContactUs.objects.all()
        ret = list()
        for contact in contact_us:
            ret.append(
                {
                    "id": contact.id,
                    "first_name": contact.first_name,
                    "last_name": contact.last_name,
                    "email": contact.email,
                    "message": contact.message,
                    "created_at": contact.created_at
                }
            )
        return self.send_success_response(message="Success", payload=ret)

    def delete(self, request, *args, **kwargs):
        if "id" in request.query_params:
            ContactUs.objects.filter(
                id=request.query_params.get("id")).delete()
        return self.send_success_response(message="Success")


class ChangeCurrentPasswordView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, requset, *args, **kwargs):
        user = requset.user
        if not user.check_password(requset.data.get("current_password")):
            return self.send_response(
                success=False,
                message=ResponseMessages.INVALID_PASSWORD,
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        if not requset.data.get("new_password") == requset.data.get("confirm_password"):
            return self.send_response(
                success=False,
                message=ResponseMessages.PASSWORD_MISMATCH,
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        user.set_password(requset.data.get("new_password"))
        user.save()
        return self.send_success_response(message="Success")


class ForgotPassword(BaseAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        import uuid
        FRONTEND_URL = "mush-app.herokuapp.com"
        user = User.objects.filter(email=request.data.get("email")).first()
        if user:
            token = str(uuid.uuid4().hex)
            token = token.replace("=", "").replace("&", "")
            user.reset_password_token = token
            user.save()
            url = FRONTEND_URL + "/change-password.html?reset_token=" + token
            body = "Click on the link to reset your password <a href='" + \
                url + "'>Reset Password</a>"
            try:
                send_mail("Reset Password: ", body,
                          EMAIL_HOST_USER, [user.email])
            except Exception as e:
                print(e)

            print(url)
        return self.send_success_response(message="Success")

    def patch(self, request, *args, **kwargs):
        if not "reset_token" in request.data:
            return self.send_response(
                success=False,
                message=ResponseMessages.INVALID_TOKEN,
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        user = User.objects.filter(
            reset_password_token=request.data.get("reset_token")).first()
        if not user:
            return self.send_response(
                success=False,
                message=ResponseMessages.INVALID_TOKEN,
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        user.set_password(request.data.get("password"))
        user.save()
        return self.send_success_response(message="Success")
