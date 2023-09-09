from django.db import transaction

from django.core.mail import EmailMultiAlternatives

from rest_framework_simplejwt.tokens import RefreshToken
from common.services import model_update
from .models import User


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }

def email_send(user, uidb64, token):
    subject = "Reset your password"
    from_email = "support@bookmarks.net"
    to = [user.email]
    url = f"http://localhost:8082/reset/password?uidb64={uidb64}&token={token}"
    html = f"You have a requested to reset your password. Please click the link below to reset your password. The link is {url}."
    plain_text = f"You have a requested to reset your password. Please click the link below to reset your password. The link is {url}."

    msg = EmailMultiAlternatives(subject, plain_text, from_email, to)
    msg.attach_alternative(html, "text/html")

    msg.send()

    return 


@transaction.atomic
def user_update(*, user: User, data) -> User:
    non_side_effect_fields = []

    user, has_updated = model_update(instance=user, fields=non_side_effect_fields, data=data)

    return user
