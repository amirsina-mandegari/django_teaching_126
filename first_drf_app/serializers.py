from rest_framework import serializers


class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    manager_name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(min_value=0)