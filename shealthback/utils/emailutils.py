from django.conf import settings
from django.core.mail import send_mail


def health_send_mail(subject, message, email):
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)