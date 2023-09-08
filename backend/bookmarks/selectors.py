from django.db.models.query import QuerySet

from .filters import (
    BaseBookmarkFilter
)
from .models import Bookmark

def bookmark_list(*, filters=None) -> QuerySet[Bookmark]:
    filters = filters or {}

    qs = Bookmark.objects.all()

    return BaseBookmarkFilter(filters, qs).qs
