from django.db import models

# Create your models here.

class Usertype(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_category = models.CharField

class HealthUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile = models.IntegerField(max_length=10)
    user_category = models.ForeignKey(Usertype, on_delete=models.DO_NOTHING)

class HealthUserSessions(models.Model):
    health_user_session_id = models.AutoField(primary_key=True)
    healthuser = models.ForeignKey(HealthUser, on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=100)



