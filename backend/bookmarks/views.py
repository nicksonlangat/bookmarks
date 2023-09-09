from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView, ListAPIView, 
    RetrieveUpdateAPIView, 
    RetrieveDestroyAPIView
)

from rest_framework.permissions import IsAuthenticated

from common.pagination import (
    PageNumberPagination,
    get_paginated_response
)
from .selectors import bookmark_list
from .services import bookmark_create, bookmark_update

from .models import Bookmark
from .serializers import BookmarkSerializer

class BookmarkApi(
    CreateAPIView, ListAPIView, 
    RetrieveUpdateAPIView, RetrieveDestroyAPIView):

    # permission_classes = [IsAuthenticated]

    serializer_class = BookmarkSerializer

    class Pagination(PageNumberPagination):
        default_limit = 16

    queryset = bookmark_list()

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        # serializer.validated_data.pop("user")
        bookmark_create(serializer.validated_data)
        return Response({"message": "bookmark added" }, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        filters = request.query_params
        qs = bookmark_list(filters=filters)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.serializer_class,
            queryset=qs,
            request=request,
            view=self,
        )

    def patch(self, request, pk, format=None):  
        bookmark = Bookmark.objects.get(id=pk)
        serializer = self.serializer_class(bookmark, data=request.data)
        if serializer.is_valid():
            bookmark_update(bookmark, data=serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        bookmark = Bookmark.objects.get(id=pk)
        bookmark.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
