from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenBlacklistSerializer,
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)


class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(
        required=True, min_length=8, write_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password_confirmation')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    @staticmethod
    def validate(attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})
        return attrs

    def create(self, validated_data):
        del validated_data['password_confirmation']
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class UpdatePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=True, min_length=8)
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    password_confirmation = serializers.CharField(
        write_only=True, required=True, min_length=8
    )

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password_confirmation')

    def validate_old_password(self, value):
        if not self.instance.check_password(value):
            raise serializers.ValidationError('Old password is incorrect.')
        return value

    @staticmethod
    def validate(attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})
        return attrs

    def update(self, instance, validated_data):
        del validated_data['old_password']
        del validated_data['password_confirmation']
        validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['refresh_token'] = data.pop('refresh')
        data['token'] = data.pop('access')
        return data


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    refresh_token = serializers.CharField(required=True)
    refresh = None

    def validate(self, attrs):
        attrs['refresh'] = attrs.pop('refresh_token')
        data = super().validate(attrs)
        data['refresh_token'] = data.pop('refresh')
        data['token'] = data.pop('access')
        return data


class CustomTokenBlacklistSerializer(TokenBlacklistSerializer):
    refresh_token = serializers.CharField(required=True)
    refresh = None

    def validate(self, attrs):
        attrs['refresh'] = attrs.pop('refresh_token')
        return super().validate(attrs)
