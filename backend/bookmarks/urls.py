from django.urls import path

from .views import BookmarkApi, ColorApi

urlpatterns = [
    # bookmark endpoints
    path("bookmarks", BookmarkApi.as_view(), name="bookmarks"),
    path("bookmarks/<uuid:pk>/", BookmarkApi.as_view(), name="bookmark"),

    path("colors", ColorApi.as_view(), name="colors"),
    path("colors/<uuid:pk>/", ColorApi.as_view(), name="color"),
]
