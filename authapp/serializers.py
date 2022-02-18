from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'role', 'is_staff', 'is_active', 'birth', 'groups']


class UserSerializerCreate(serializers.ModelSerializer):
    password_confirm = serializers.CharField(max_length=100, write_only=True)
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'email', 'first_name', 'last_name', 'birth']

    def validate(self, attrs):
        password = attrs['password']
        password2 = attrs['password_confirm']

        if password != password2:
            raise serializers.ValidationError('passwords are different')
        else:
            return attrs

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise serializers.ValidationError('username exists')

    def validate_email(self, email):
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise serializers.ValidationError('email exists')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            birth=validated_data['birth'])
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
