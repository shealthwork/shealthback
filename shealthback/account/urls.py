from django.urls import path
from .session_api import *

urlpatterns = [
    path('verify/<contact>', Login.as_view()),
]