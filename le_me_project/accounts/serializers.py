from rest_framework.serializers import Serializer
from rest_framework import serializers

class AuthSerializer(Serializer):
    username = serializers.CharField(max_length=100)
    password =  serializers.CharField(max_length=100)

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)