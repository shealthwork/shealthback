import email
from os import stat
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from django.forms.models import model_to_dict
from .models import HealthUser, HealthUserSessions, Usertype
import utils.jsonutils as JsonUtils
import utils.httputils as HttpUtils
import account.handlers as AccountHandlers

CONTACT_TYPE = "contact_type"
CONTACT_TYPE_MOBILE = "mobile"
CONTACT_TYPE_EMAIL = "email"

CLIENT_USER_TYPE = 3
VENDOR_USER_TYPE = 4


class Login(APIView):
    """
    Login class for Users
    """

    def post(self, request, contact):
        """
        Return a list of all users.
        """
        request_data = HttpUtils.get_request_msg(request)
        request_data = JsonUtils.parse_json_data(request_data)

        otp = request_data.get("otp", None)

        if otp:
            otp_flag = AccountHandlers.verify_otp(contact, otp)

        if otp_flag:
            try:
                health_user_profile = HealthUser.objects.get(email=contact)
            except Exception as err:
                print("User with email " + contact + " not Found. Creating one")
                user_type = Usertype.objects.get(user_id=CLIENT_USER_TYPE)
                health_user_profile = HealthUser.objects.create(
                    email=contact, user_category=user_type
                )

            token = health_user_profile.generate_token(request)
            user_dict = model_to_dict(health_user_profile)
            user_dict.update({"token": token})
            return Response(status=status.HTTP_200_OK, data=user_dict)
        else:
            return Response(
                {"message": "Incorrect OTP"}, status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request, contact):
        """
        Generate OTP for the user login or registration
        """
        print("here")

        contact_type = request.GET.get(CONTACT_TYPE, None)

        AccountHandlers.generate_otp(contact, contact_type)

        return Response(
            data={"message": "successfully OTP Generated"}, status=status.HTTP_201_CREATED
        )


class Logout(APIView):
    """
    Logout class for Users
    """

    def get(self, request):
        """
        Logout
        """
        token = request.GET.get("token", None)

        if token:
            try:
                healthuser_session = HealthUserSessions.objects.get(token=token)
            except Exception as err:
                print(str(err))
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
            healthuser_session.delete()
            return Response(status=status.HTTP_200_OK)
            

