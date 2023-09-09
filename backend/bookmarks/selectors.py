from django.db.models.query import QuerySet

from .filters import (
    BaseBookmarkFilter
)
from .models import Bookmark

def bookmark_list(*, filters=None, user) -> QuerySet[Bookmark]:
    filters = filters or {}

    qs = Bookmark.objects.filter(user=user)

    return BaseBookmarkFilter(filters, qs).qs
