from django.urls import path

from .views import BookmarkApi

urlpatterns = [
    # bookmark endpoints
    path("bookmarks", BookmarkApi.as_view(), name="bookmarks"),
    path("bookmarks/<uuid:pk>/", BookmarkApi.as_view(), name="bookmark"),
]
