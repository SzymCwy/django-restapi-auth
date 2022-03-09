from .serializers import Userserializer, UserSerializerUpdate, UserSerializerCreate, LoginSerializer
from rest_framework import generics
from .models import User
from rest_framework.permissions import BasePermission, AllowAny


class UserList(generics.ListAPIView):
    serializer_class = Userserializer
    queryset = User.objects.all()


class UserDetail(generics.RetrieveAPIView):
    serializer_class = Userserializer
    queryset = User.objects.all()


class UserUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializerUpdate
    queryset = User.objects.all()


class UserCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializerCreate
    queryset = User.objects.all()


class Login(generics.RetrieveAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()
