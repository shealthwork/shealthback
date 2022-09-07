import utils.emailutils as EmailUtils
from .models import HealthUserOtp
import random


CONTACT_TYPE_MOBILE = "mobile"
CONTACT_TYPE_EMAIL = "email"


def generate_otp(contact, contact_type):

    otp = random.randint(100000, 999999)

    if contact_type == CONTACT_TYPE_EMAIL:
        try:
            health_otp_profile = HealthUserOtp.objects.get(contact=contact)
            print(health_otp_profile)
        except Exception as err:
            health_otp_profile = HealthUserOtp.objects.create(contact=contact, otp=otp)
        if health_otp_profile:
            health_otp_profile.otp = otp
            health_otp_profile.save()

        subject = 'OTP Verfication - SHealth'
        message = f'Hi {contact}, Your OTP is {otp}.'

        print(otp)

        # EmailUtils.health_send_mail(subject, message, contact)


def verify_otp(contact, otp):
    try:
        print(contact)
        health_otp_profile = HealthUserOtp.objects.get(contact=contact)

        if str(health_otp_profile.otp) == str(otp):
            return True
        else:
            False
    except Exception as err:
        print("here")
        print(err)
        return False
