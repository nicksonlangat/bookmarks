import django_filters
from .models import Bookmark, Color

class BaseBookmarkFilter(django_filters.FilterSet):
    class Meta:
        model = Bookmark
        fields = ("id", "title")


class BaseColorFilter(django_filters.FilterSet):
    class Meta:
        model = Color
        fields = ("id", "code")
