from rest_framework import status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView
)
from rest_framework.permissions import IsAuthenticated

from .serializers import UserRegisterSerializer, UserSerializer
from .models import User

from .services import get_tokens_for_user



class UserRegisterApi(CreateAPIView):

    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginApi(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        response = Response()
        if (email is None) or (password is None):
            raise exceptions.AuthenticationFailed("email and password required")
        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed("user not found")
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("wrong password")

        token = get_tokens_for_user(user)
        response.data = token
        return response

class UserMeApi(RetrieveAPIView): 
        serializer_class = UserSerializer
        model = User
        permission_classes = [IsAuthenticated]

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj
        