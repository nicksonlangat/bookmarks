from django.db import transaction
from rest_framework_simplejwt.tokens import RefreshToken
from common.services import model_update
from .models import User


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


@transaction.atomic
def user_update(*, user: User, data) -> User:
    non_side_effect_fields = []

    user, has_updated = model_update(instance=user, fields=non_side_effect_fields, data=data)

    # Side-effect fields update here (e.g. username is generated based on first & last name)

    # ... some additional tasks with the user ...

    return user
