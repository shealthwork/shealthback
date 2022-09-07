from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(HealthUser)
admin.site.register(HealthUserOtp)
admin.site.register(HealthUserSessions)
admin.site.register(Usertype)
