import django_filters
from .models import Bookmark

class BaseBookmarkFilter(django_filters.FilterSet):
    class Meta:
        model = Bookmark
        fields = ("id", "title",)
