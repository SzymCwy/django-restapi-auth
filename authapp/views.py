from .serializers import Userserializer, UserSerializerUpdate, UserSerializerCreate, LoginSerializer
from rest_framework import generics
from .models import User
<<<<<<< HEAD
from rest_framework.permissions import BasePermission, AllowAny
=======
from rest_framework.permissions import AllowAny
>>>>>>> 5647d9303597d12ed639960286631e4ae957807f


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
