from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView, ListAPIView, 
    RetrieveUpdateAPIView, 
    RetrieveDestroyAPIView
)

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import Http404

from common.pagination import (
    PageNumberPagination,
    get_paginated_response
)
from .selectors import bookmark_list, color_list
from .services import bookmark_create, bookmark_update, color_create, color_update

from .models import Bookmark, Color
from .serializers import BookmarkSerializer, ColorSerializer


class ColorApi(APIView):
    class Pagination(PageNumberPagination):
        page_size = 12
    
    serializer_class = ColorSerializer

    def get_object(self, pk):
        try:
            return Color.objects.get(pk=pk)
        except Color.DoesNotExist:
            raise Http404
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            color = color_create(request.data)
            return Response(data={"id": color.id}, status=status.HTTP_201_CREATED)
        
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get(self, request, format=None):
        colors = color_list(filters=request.query_params)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=ColorSerializer,
            queryset=colors,
            request=request,
            view=self
        )
    
    def delete(self, request, pk, format=None):
        color = self.get_object(pk)
        color.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookmarkApi(
    CreateAPIView, ListAPIView, 
    RetrieveUpdateAPIView, RetrieveDestroyAPIView):

    permission_classes = [IsAuthenticated]

    serializer_class = BookmarkSerializer

    class Pagination(PageNumberPagination):
        default_limit = 16

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        bookmark_create(serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        filters = request.query_params
        qs = bookmark_list(filters=filters, user=request.user)

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
