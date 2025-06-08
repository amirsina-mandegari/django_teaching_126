from rest_framework import serializers
from first_drf_app.models import Company


class CompanySerializer(serializers.ModelSerializer):
    age_in_days = serializers.SerializerMethodField()
    age_in_month = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Company
        exclude = ('id',)

    def get_age_in_days(self, obj):
        return obj.age * 365


class CreateCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ('id', 'employees')