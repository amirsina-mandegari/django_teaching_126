from rest_framework import serializers
from django.contrib.auth import authenticate


class TokenAuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=100, min_length=1, write_only=True)
    password = serializers.CharField(required=True, max_length=100, min_length=1, write_only=True)

    def validate(self, attrs):
        username=attrs['username']
        password=attrs['password']
        user = authenticate(self.context['request'], username=username, password=password)
        if not user:
            raise serializers.ValidationError('user name or password is wrong!')
        attrs['user'] = user
        return attrs
    