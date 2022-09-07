from operator import concat
from django.db import models
import random
import string

# Create your models here.

class Usertype(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_category = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.user_category


class HealthUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    mobile = models.IntegerField(max_length=10, default=1234567890)
    email = models.CharField(max_length=100, default="")
    user_category = models.ForeignKey(Usertype, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.email    

    def generate_token(self, request):

        email = self.email
        string_lenth = 16
        token = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=string_lenth)
        )

        health_user_profile = HealthUser.objects.get(email=email)

        health_user_session_profile, _ = HealthUserSessions.objects.get_or_create(
            healthuser=health_user_profile
        )
        health_user_session_profile.token = token
        health_user_session_profile.save()

        return token


class HealthUserSessions(models.Model):
    health_user_session_id = models.AutoField(primary_key=True)
    healthuser = models.ForeignKey(HealthUser, on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.healthuser.email


class HealthUserOtp(models.Model):
    contact = models.CharField(max_length=100)
    otp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact
