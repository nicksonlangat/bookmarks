from django.db.models.query import QuerySet

from .filters import (
    BaseBookmarkFilter, BaseColorFilter
)
from .models import Bookmark, Color

def bookmark_list(*, filters=None, user) -> QuerySet[Bookmark]:
    filters = filters or {}

    qs = Bookmark.objects.filter(user=user)

    return BaseBookmarkFilter(filters, qs).qs


def color_list(*, filters=None) -> QuerySet[Color]:
    filters = filters or {}

    qs = Color.objects.all()

    return BaseColorFilter(filters, qs).qs
